import psycopg2
import os
import time
import random
import string
from datetime import timedelta, datetime

# Получаем URL базы данных из переменных окружения (Heroku автоматически добавит DATABASE_URL)
DATABASE_URL = os.getenv('DATABASE_URL')

def connect_db():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            subscription INTEGER DEFAULT 0,
            subscription_end_time TIMESTAMP,
            image_limit INTEGER DEFAULT 0,
            image2_limit INTEGER DEFAULT 0,
            upscale_limit INTEGER DEFAULT 0,
            reimage_limit INTEGER DEFAULT 0,
            expand_limit INTEGER DEFAULT 0,
            background_limit INTEGER DEFAULT 0,
            snap_limit INTEGER DEFAULT 0,
            vision_limit INTEGER DEFAULT 0,
            invite_value INTEGER DEFAULT 0,
            invite_code TEXT DEFAULT NULL,
            last_search_time INTEGER DEFAULT 0,
            last_CheckPaymentStatus_button INTEGER DEFAULT 0,
            snap_coins INTEGER DEFAULT 0,
            language TEXT DEFAULT 'en'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS frozen_users (
            user_id BIGINT PRIMARY KEY,
            timestamp BIGINT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS processed_users (
            user_id BIGINT PRIMARY KEY,
            timestamp BIGINT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paying_users (
            user_id BIGINT PRIMARY KEY,
            timestamp BIGINT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dialog_history (
        id SERIAL PRIMARY KEY,
        user_id BIGINT,
        message TEXT,
        role TEXT,
        timestamp TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users_config (
        user_id BIGINT PRIMARY KEY,
        image_model TEXT DEFAULT 'black-forest-labs/FLUX.1-schnell',
        text_model TEXT DEFAULT 'mistral-large-latest'
        )
    ''')

    migrate_database()
    migrate_users_config(cursor)
    conn.commit()
    conn.close()

def migrate_users_config(cursor):
    cursor.execute('''
        INSERT INTO users_config (user_id)
        SELECT user_id FROM users
        ON CONFLICT (user_id) DO NOTHING
    ''')

def initialize_database():
    create_tables()

def migrate_database():
    conn = connect_db()
    cursor = conn.cursor()
    # Список новых столбцов с их типами
    
    new_columns = {
        'upscale_limit': 'INTEGER DEFAULT 0',
        'background_limit': 'INTEGER DEFAULT 0',
        'reimage_limit': 'INTEGER DEFAULT 0',
        'expand_limit': 'INTEGER DEFAULT 0',
        'invite_value': 'INTEGER DEFAULT 0',
        'invite_code': 'TEXT DEFAULT NULL',
        'last_search_time': 'INTEGER DEFAULT 0',
        'last_checkpaymentstatus_button': 'INTEGER DEFAULT 0',
        'snap_coins': 'INTEGER DEFAULT 0',
        'language': 'TEXT DEFAULT \'en\'',
    }
    # Проверка существующих столбцов в таблице users
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name='users'")
    existing_columns = [row[0] for row in cursor.fetchall()]
    
    # Добавление недостающих столбцов
    for column_name, column_type in new_columns.items():
        if column_name not in existing_columns:
            cursor.execute(f"ALTER TABLE users ADD COLUMN {column_name} {column_type}")

    cursor.execute('''
        ALTER TABLE dialog_history ALTER COLUMN user_id TYPE BIGINT
    ''')
    conn.commit()
    conn.close()

def register_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute('INSERT INTO users (user_id) VALUES (%s)', (user_id,))
        cursor.execute('INSERT INTO users_config (user_id) VALUES (%s)', (user_id,))
        conn.commit()
        return True
    return False

def get_stats():
    conn = connect_db()
    cursor = conn.cursor()
    # Получаем количество всех пользователей
    cursor.execute('SELECT COUNT(*) FROM users')
    total_users = cursor.fetchone()[0]
    # Получаем количество замороженных пользователей
    cursor.execute('SELECT COUNT(*) FROM frozen_users')
    frozen_users = cursor.fetchone()[0]
    # Получаем количество пользователей, которые сейчас генерируют что-то
    cursor.execute('SELECT COUNT(*) FROM processed_users')
    processing_users = cursor.fetchone()[0]
    # Получаем количество платных подписчиков
    cursor.execute('SELECT COUNT(*) FROM users WHERE subscription > 0')
    paying_users = cursor.fetchone()[0]
    # Получаем список всех колонок с суффиксом '_limit' из таблицы users
    cursor.execute("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'users' AND column_name LIKE '%_limit'
    """)
    limit_columns = [row[0] for row in cursor.fetchall()]
    # Суммируем значения для каждой колонки с суффиксом '_limit'
    limits = {}
    for column in limit_columns:
        cursor.execute(f'SELECT COALESCE(SUM({column}), 0) FROM users')
        limit_name = column.replace('_limit', '')
        limits[limit_name] = cursor.fetchone()[0]
    
    cursor.execute('SELECT user_id FROM users')
    user_ids = [row[0] for row in cursor.fetchall()]

    conn.close()
    return {
        'total_users': total_users,
        'frozen_users': frozen_users,
        'processing_users': processing_users,
        'paying_users': paying_users,
        'limits': limits,
        'user_ids': user_ids
    }

def is_user_registered(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
    return cursor.fetchone() is not None

def is_user_frozen(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM frozen_users WHERE user_id = %s', (user_id,))
    return cursor.fetchone() is not None

def freeze_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    timestamp = int(time.time())
    cursor.execute('INSERT INTO frozen_users (user_id, timestamp) VALUES (%s, %s)', (user_id, timestamp))
    conn.commit()
    conn.close()

def unfreeze_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    current_time = int(time.time())
    cursor.execute('DELETE FROM frozen_users WHERE user_id = %s', (user_id,))
    conn.commit()
    conn.close()

def has_subscription(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT subscription FROM users WHERE user_id = %s', (user_id,))
    user = cursor.fetchone()
    if user and user[0] == 1:
        return True
    return False

def update_subscription(user_id, sub_status):
    conn = connect_db()
    cursor = conn.cursor()
    current_time = int(time.time())
    month = 31 * 24 * 60 * 60
    end_time = current_time + month
    end_time_ts = datetime.fromtimestamp(end_time)
    cursor.execute(
        'UPDATE users SET subscription = %s, subscription_end_time = %s WHERE user_id = %s',
        (sub_status, end_time_ts, user_id)
    )
    conn.commit()

def user_set_lang(user_id, lang):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET language = %s WHERE user_id = %s', (lang, user_id))
    conn.commit()
    conn.close()

def user_get_lang(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT language FROM users WHERE user_id = %s', (user_id,))
    user_lang = cursor.fetchone()
    conn.close()
    return user_lang[0]

def user_set_config(user_id, config, model):
    conn = connect_db()
    cursor = conn.cursor()
    column = None
    if config == "IGM":
        column = "image_model"
    elif config == "TGM":
        column = "text_model"
    if column:
        cursor.execute(f"UPDATE users_config SET {column} = %s WHERE user_id = %s", (model, user_id))
        conn.commit()
    conn.close()

def user_get_config(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT image_model, text_model FROM users_config WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    return result

def give_coins(user_id, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE users SET snap_coins = snap_coins + %s WHERE user_id = %s',
        (amount*10, user_id)
    )
    conn.commit()

def get_coin_value(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT snap_coins FROM users WHERE user_id = %s', (user_id,))
    user_coins = cursor.fetchone()
    conn.close()
    return user_coins[0]

async def check_subscriptions():
    conn = connect_db()
    cursor = conn.cursor()
    current_time = datetime.now()
    cursor.execute('''
        UPDATE users 
        SET subscription = 0, subscription_end_time = NULL 
        WHERE subscription_end_time < %s
    ''', (current_time,))
    conn.commit()
    conn.close()

async def reset_limits():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users 
        SET image_limit = 0, image2_limit = 0, snap_limit = 0, vision_limit = 0, upscale_limit = 0, background_limit = 0, expand_limit = 0, reimage_limit = 0
    ''')
    conn.commit()
    conn.close()

def get_limits(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT image_limit, image2_limit, snap_limit, vision_limit, upscale_limit, background_limit, expand_limit, reimage_limit FROM users WHERE user_id = %s', (user_id,))
    limits = cursor.fetchone()
    conn.close()
    return limits

def get_last_search_time(user_id, button: bool = False):
    conn = connect_db()
    cursor = conn.cursor()
    if button:
        cursor.execute('SELECT last_checkpaymentstatus_button FROM users WHERE user_id = %s', (user_id,))
    else:
        cursor.execute('SELECT last_search_time FROM users WHERE user_id = %s', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0

def update_last_search_time(user_id, timestamp, button: bool = False):
    conn = connect_db()
    cursor = conn.cursor()
    if button:
        cursor.execute('UPDATE users SET last_checkpaymentstatus_button = %s WHERE user_id = %s', (timestamp, user_id))
    else:
        cursor.execute('UPDATE users SET last_search_time = %s WHERE user_id = %s', (timestamp, user_id))
    conn.commit()
    conn.close()

def invite_code_check(referral_code):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM users WHERE invite_code = %s', (referral_code,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def set_invite_value(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    current_value = get_invite_value(user_id)
    new_value = current_value + 1
    cursor.execute('UPDATE users SET invite_value = %s WHERE user_id = %s', (new_value, user_id))
    conn.commit()
    conn.close()

def set_invite_value_minus_5(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    current_value = get_invite_value(user_id)
    new_value = current_value - 5
    cursor.execute('UPDATE users SET invite_value = %s WHERE user_id = %s', (new_value, user_id))
    conn.commit()
    conn.close()

def get_invite_value(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT invite_value FROM users WHERE user_id = %s', (user_id,))
    invite_value = cursor.fetchone()
    conn.close()
    return invite_value[0]

def get_invite_code(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT invite_code FROM users WHERE user_id = %s', (user_id,))
    result = cursor.fetchone()
    if result and result[0]:
        invite_code = result[0]
    else:
        invite_code = generate_unique_invite_code()
        cursor.execute('UPDATE users SET invite_code = %s WHERE user_id = %s', (invite_code, user_id))
        conn.commit()
    conn.close()
    return invite_code

def generate_unique_invite_code(length=8):
    characters = string.ascii_letters + string.digits
    while True:
        invite_code = ''.join(random.choice(characters) for _ in range(length))
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM users WHERE invite_code = %s', (invite_code,))
        exists = cursor.fetchone()
        conn.close()
        if not exists:
            return invite_code

def limit_reached(user_id, limit_column, max_limit):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'SELECT {limit_column} FROM users WHERE user_id = %s', (user_id,))
    limit_value = cursor.fetchone()[0]
    
    if limit_value >= max_limit:
        return True
    return False

def increment_limit(user_id, limit_column, value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'SELECT {limit_column} FROM users WHERE user_id = %s', (user_id,))
    limit_value = cursor.fetchone()[0]
    cursor.execute(f'UPDATE users SET {limit_column} = %s WHERE user_id = %s', (limit_value + value, user_id))
    conn.commit()

def set_processing(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO processed_users (user_id, timestamp) 
        VALUES (%s, %s) ON CONFLICT (user_id) DO UPDATE 
        SET timestamp = EXCLUDED.timestamp
    ''', (user_id, time.time()))
    conn.commit()
    conn.close()

def is_processing(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT timestamp FROM processed_users WHERE user_id = %s', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def set_paying(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    timestamp = int(time.time())
    cursor.execute('''
        INSERT INTO paying_users (user_id, timestamp) 
        VALUES (%s, %s) ON CONFLICT (user_id) DO UPDATE 
        SET timestamp = EXCLUDED.timestamp
    ''', (user_id, timestamp))
    conn.commit()
    conn.close()

def is_paying(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT timestamp FROM paying_users WHERE user_id = %s', (user_id,))
    result = cursor.fetchone()
    
    if result:
        current_time = int(time.time())
        if current_time - result[0] < 900:
            return True
        else:
            cursor.execute('DELETE FROM paying_users WHERE user_id = %s', (user_id,))
            conn.commit()
    
    conn.close()
    return False

def save_dialog_message(user_id, message, role):
    conn = connect_db()
    cursor = conn.cursor()
    timestamp = int(time.time())
    cursor.execute('INSERT INTO dialog_history (user_id, message, role, timestamp) VALUES (%s, %s, %s, %s)', (user_id, message, role, timestamp))
    conn.commit()
    conn.close()

def get_dialog_history(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT message, role FROM dialog_history WHERE user_id = %s ORDER BY timestamp ASC', (user_id,))
    history = cursor.fetchall()
    conn.close()
    return history

async def clear_dialog_history():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dialog_history')
    conn.commit()
    conn.close()

def clear_processing(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM processed_users WHERE user_id = %s', (user_id,))
    conn.commit()
    conn.close()

def clear_all_processing():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM processed_users')
    conn.commit()
    conn.close()
