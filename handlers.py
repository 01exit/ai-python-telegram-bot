import os
import snap_utils.keyboards as KeyBoard
import time
from snap_utils.cryptomus import create_invoice, get_invoice
from aiogram.utils.keyboard import InlineKeyboardBuilder
from snap_utils.config import HF_SUBSCRIPTION_MODELS, info_dict, version
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BufferedInputFile, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from snap_utils.captcha import generate_captcha
from snap_utils.database import (
    register_user, 
    is_user_registered, 
    has_subscription, 
    update_subscription,
    is_user_frozen, 
    freeze_user,
    set_processing,
    unfreeze_user,
    get_last_search_time,
    update_last_search_time,
    invite_code_check,
    get_invite_code,
    get_invite_value,
    set_invite_value,
    set_invite_value_minus_5,
    set_paying,
    get_stats,
    give_coins,
    get_coin_value,
    user_set_lang,
    user_get_lang,
    user_get_config,
    user_set_config
)
from snap_actions.image_generator_HF import main_image_generator
from snap_actions.image_generator_BRIA import main_bria_generation
from snap_actions.bria_background_change import main_bria_background_change
from snap_actions.bria_upscaling import main_bria_upscaling
from snap_actions.bria_expand import main_bria_image_expand
from snap_actions.bria_reimage import main_bria_reimage
from snap_actions.snap_generate import mistral_generate
from snap_actions.snap_vision import image_vision
from snap_utils.limits import limits_get
from snap_utils.checker import check_user_status, inputs_checker
from snap_actions.search import main_search_query
from snap_utils.utils import translation

load_dotenv()
TOKEN = os.getenv('TOKEN')
PAYMENT_PROVIDER_TOKEN = os.getenv('PAYMENT_PROVIDER_TOKEN')

router = Router()

class Promt(StatesGroup):
    awaiting_captcha = State()
    image1 = State()
    image1_num_images = State()
    image1_final = State()
    bria_image_generation = State()
    bria_image_upscale = State()
    mistral_vision = State()
    bria_background = State()
    bria_background_prompt = State()
    bria_reimage_prompt = State()
    bria_reimage = State()
    bria_expand = State()
    lang_choose = State()
    config_wait = State()
    config_set = State()
async def send_captcha(user_id, message: Message, state: FSMContext, referral_code):
    captcha_text, captcha_image = generate_captcha()
    await state.update_data(captcha=captcha_text, referral_code=referral_code)
    captcha_image.seek(0)
    photo = BufferedInputFile(captcha_image.read(), filename="captcha.png")
    await message.answer_photo(photo=photo, caption=f"Enter text from captcha")
    await state.set_state(Promt.awaiting_captcha)

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    args = message.text.split()[1] if len(message.text.split()) > 1 else None
    referral_code = args if args else None
    if referral_code:
        await register(message, state, referral_code)
    else:
        await message.answer('Hello, I am *Snaplix Bot*. I create *AI content*. Enter command /reg to register', parse_mode='Markdown')

@router.message(Command('reg'))
async def register(message: Message, state: FSMContext, referral_code = None):
    user_id = message.from_user.id
    if is_user_frozen(user_id):
        await message.answer("You are temporarily blocked. Please try again later.")
        return
    state_data = await state.get_data()
    if 'registration_in_progress' in state_data:
        await message.answer("You are already in the process of registration. Please complete it.")
        return
    if is_user_registered(user_id):
        user_lang = user_get_lang(user_id)
        await message.answer(translation(user_lang, "already_registered"))
        return
    await state.update_data(registration_in_progress=True, reg_attempts=0)
    await send_captcha(user_id, message, state, referral_code)

@router.message(Promt.awaiting_captcha)
async def check_captcha(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if is_user_frozen(user_id):
        await message.answer("You have been blocked. Write to the user @wirex663 in private messages to unblock")
        return
    data = await state.get_data()
    referral_code = data['referral_code']
    if message.text.upper() == data['captcha']:
        await message.answer("You have *successfully registered!*\nUse the command /info <bot command> to get full information about the command", parse_mode='Markdown')
        register_user(user_id)
        await message.bot.send_message(chat_id=905207082, text="New user has been registred!")
        if referral_code is not None:
            inviter_user_id = invite_code_check(referral_code)
            if inviter_user_id:
                user_lang = user_get_lang(int(inviter_user_id))
                await message.bot.send_message(chat_id=int(inviter_user_id), text=translation(user_lang, "invitee_registered"))
                set_invite_value(inviter_user_id)
        await state.clear()
    else:
        attempts = data.get('reg_attempts', 0) + 1
        await state.update_data(reg_attempts=attempts)
        if attempts >= 4:
            freeze_user(user_id)
            await message.answer("You have *failed registration* after 4 attempts.")
            await state.clear()
        else:
            await message.answer(f"Incorrect. Attempts left: {4 - attempts}.")
            await send_captcha(user_id, message, state, referral_code)

#@router.message(Command('sub'))
#async def check_subscription(message: Message):
    #if await check_user_status(message):
        #return
    #if has_subscription(message.from_user.id):
        #await message.answer("You *have* an active subscription!", parse_mode='Markdown')
    #else:
        #await message.answer("You *do not have* an active subscription.", parse_mode='Markdown')

@router.message(Command('invite'))
async def invite(message: Message):
    if await check_user_status(message):
        return
    invite_code = get_invite_code(message.from_user.id)
    user_lang = user_get_lang(message.from_user.id)
    await message.answer(translation(user_lang, "invite_link").format(link=f"https://t.me/snaplixbot?start={invite_code}"))

@router.message(Command('my_invites'))
async def my_invites(message: Message):
    if await check_user_status(message):
        return
    invites = get_invite_value(message.from_user.id)
    user_lang = user_get_lang(message.from_user.id)
    await message.answer(translation(user_lang, "my_invites").format(invites=invites), parse_mode='Markdown')

@router.message(Command('my_coins'))
async def my_coins(message: Message):
    if await check_user_status(message):
        return
    coins = get_coin_value(message.from_user.id)
    user_lang = user_get_lang(message.from_user.id)
    await message.answer(translation(user_lang, "my_coins").format(coins=coins), parse_mode='Markdown')

@router.message(Command('invite_reward'))
async def invite_reward(message: Message):
    if await check_user_status(message):
        return
    invites = get_invite_value(message.from_user.id)
    user_lang = user_get_lang(message.from_user.id)
    if invites >= 5:
        give_coins(int(message.from_user.id), 5)
        set_invite_value_minus_5(int(message.from_user.id))
        await message.bot.send_message(chat_id=905207082, text="New sub by invites!")
        await message.answer(translation(user_lang, "invite_reward"))
    #elif has_subscription(message.from_user.id):
        #await message.answer("You *have* an active subscription!", parse_mode='Markdown')
    else:
        await message.answer(translation(user_lang, "less_than_5_invites"), parse_mode='Markdown')

@router.message(Command('donate'))
async def subscribe(message: Message):
    if await check_user_status(message, check_payment=True):
        return
    user_text = message.text.replace('/donate', '').strip()
    user_lang = user_get_lang(message.from_user.id)
    if not user_text:
        await message.reply(translation(user_lang, "donate_amount"))
        return
    try:
        amount = int(user_text)
        if amount < 1 or amount > 100:
            raise ValueError
    except ValueError:
        await message.reply(translation(user_lang, "invalid_donate_amount"))
        return
    invoice = await create_invoice(message.from_user.id, amount)
    if "errors" in invoice:
        await message.reply(f"Error: {invoice['errors']}")
        return
    markup = InlineKeyboardBuilder().button(
        text='Check Payment Status', callback_data=f"o_{invoice['result']['uuid']}:{invoice['user_id']}:{invoice['amount']}"
        ).as_markup()
    await message.reply(translation(user_lang, "donate_description").format(link=invoice['result']['url']), reply_markup=markup, parse_mode='Markdown')
    set_paying(message.from_user.id)

@router.callback_query(F.data.startswith("o_"))
async def check_order(query: CallbackQuery):
    uuid, user_id, amount = query.data.split(":")
    if query.from_user.id != int(user_id):
        await query.answer("You are not the owner of this invoice", show_alert=True)
        return
    current_time = int(time.time())
    user_lang = user_get_lang(query.from_user.id)
    last_CheckPaymentButton_time = get_last_search_time(query.from_user.id, button=True)
    if current_time - last_CheckPaymentButton_time < 30:
        await query.answer(translation(user_lang, "check_payment_later"), show_alert=True)
        return
    invoice = await get_invoice(uuid.split("_")[1])
    update_last_search_time(query.from_user.id, int(time.time()), button=True)
    if invoice["result"]["status"] in {"paid", "paid_over"}:
        await query.answer("")
        give_coins(int(user_id), int(amount))
        await query.message.edit_text(translation(user_lang, "donate_thank_you").format(amount=int(amount)*10, order_id=invoice['result']['order_id']), parse_mode='Markdown')
        await query.message.bot.send_message(chat_id=905207082, text=f"New donate ${amount}. Order id: {invoice['result']['order_id']}")
    elif invoice["result"]["status"] == "cancel":
        await query.message.delete()
    elif invoice["result"]["status"] == "check":
        await query.answer("")
        await query.message.answer(translation(user_lang, "order_not_paid"), parse_mode='Markdown')
    else:
        await query.answer("")
        await query.message.answer(translation(user_lang, "order_status").format(status=invoice["result"]["status"]), parse_mode="Markdown")

@router.message(Command('ping'))
async def ping_pong(message: Message):
    if await check_user_status(message):
        return
    await message.reply('![👍](tg://emoji?id=5368324170671202286)', parse_mode='MarkdownV2')

@router.message(Command('info'))
async def ping_pong(message: Message):
    if await check_user_status(message):
        return
    user_text = message.text.replace('/info', '').strip()
    user_lang = user_get_lang(message.from_user.id)
    if user_text.startswith('/'):
        user_text = user_text[1:]
    user_text = user_text.lower()
    if not user_text:
        await message.reply(translation(user_lang, "info_command_usage"))
        return
    if user_text in info_dict:
        await message.reply(translation(user_lang, "info_dict").get(user_text), parse_mode='Markdown')
    else:
        await message.reply(translation(user_lang, "command_not_found"))

#@router.message(Command('set_sub'))
#async def test(message: Message):
    #if await check_user_status(message):
        #return
    #if message.from_user.id != 905207082:
        #return
    #user_text = message.text.replace('/set_sub', '').strip()
    #if not user_text:
        #await message.reply("/set_sub <user_id>")
        #return
    #try:
        #update_subscription(int(user_text), 1)
       # await message.reply(f"Give sub to : {user_text}")
    #except Exception as e:
        #await message.reply(f"Error: {e}")

@router.message(Command('give_coins'))
async def give_coins_handler(message: Message):
    if await check_user_status(message):
        return
    if message.from_user.id != 905207082:
        return
    user_text = message.text.replace('/give_coins', '').strip()
    if not user_text:
        await message.reply("/give_coins <user_id> <amount>")
        return
    try:
        user_id, amount = map(int, user_text.split())
        if amount <= 0 or amount > 1000:
            await message.reply("Amount must be a positive integer between 1 and 1000.")
            return
        give_coins(user_id, amount)
        await message.reply(f"Given {amount} coins to user: {user_id}")
    except ValueError:
        await message.reply("/give_coins <user_id> <amount>")
    except Exception as e:
        await message.reply(f"Error: {e}")

@router.message(Command('unfreeze'))
async def test(message: Message):
    if await check_user_status(message):
        return
    if message.from_user.id != 905207082:
        return
    user_text = message.text.replace('/unfreeze', '').strip()
    if not user_text:
        await message.reply("/unfreeze <user_id>")
        return
    try:
        unfreeze_user(int(user_text))
        await message.reply(f"User {user_text} has been unfreezed")
    except Exception as e:
        await message.reply(f"Error: {e}")
    
@router.message(Command('my_id'))
async def my_id(message: Message):
    if await check_user_status(message):
        return
    user_lang = user_get_lang(message.from_user.id)
    await message.reply(translation(user_lang, "my_id").format(user_id=message.from_user.id))

@router.message(Command('limits_limits_hide'))
async def limits(message: Message):
    if await check_user_status(message):
        return
    await message.reply(await limits_get(message.from_user.id), parse_mode='Markdown')

@router.message(Command('v'))
async def info_version(message: Message):
    if await check_user_status(message):
        return
    await message.reply(version['version'], parse_mode='Markdown')

@router.message(Command('snap'))
async def snap(message: Message):
    if await check_user_status(message, limit=('snap_limit', 1000), subscription_limit=1000):
        return
    user_text = message.text.replace('/snap', '').strip()
    user_lang = user_get_lang(message.from_user.id)
    img_model, txt_model = user_get_config(message.from_user.id)
    if not user_text:
        await message.reply(translation(user_lang, "snap_ai_usage"))
        return
    reply_message = await message.reply(translation(user_lang, "thinking"), parse_mode='Markdown')
    print(message.chat.type)
    set_processing(message.from_user.id)
    await mistral_generate(reply_message, model=txt_model, user_text=user_text, user_id=message.from_user.id, chat_type=message.chat.type)
    
@router.message(Command('search'))
async def ai_search(message: Message):
    if await check_user_status(message, limit=('snap_limit', 1000), subscription_limit=1000):
        return
    current_time = int(time.time())
    last_search_time = get_last_search_time(message.from_user.id)
    user_lang = user_get_lang(message.from_user.id)
    if current_time - last_search_time < 60:
        await message.reply(translation(user_lang, "search_limit"), parse_mode='Markdown')
        return
    user_text = message.text.replace('/search', '').strip()
    if not user_text:
        await message.reply(translation(user_lang, "search_usage"))
        return
    reply_message = await message.reply(translation(user_lang, "checking_request"), parse_mode='Markdown')
    set_processing(message.from_user.id)
    msg_for_checking = (
        f'У пользователя есть следующий запрос: {user_text}\n'
        f'Если запрос пользователя является этически приемлимым и не содержит опасных или радикальных высказываний, то напиши "Yes". Если запрос содержит опасные или радикальные высказывания, такие как призывы к насилию, терроризму, незаконной деятельности или дискриминации, то напиши "No"'
    )
    checking_response = await mistral_generate(reply_message, model="mistral-large-latest", user_text=msg_for_checking, user_id=message.from_user.id, chat_type=message.chat.type, save_dialog=False, hide=True)
    if "No" in checking_response:
        await reply_message.edit_text(translation(user_lang, "unethical_request"), parse_mode='Markdown')
    else:
        await reply_message.edit_text(translation(user_lang, "searching"), parse_mode='Markdown')
        msg_for_mistral_ai = await main_search_query(user_text)
        await mistral_generate(reply_message, model="mistral-large-latest", user_text=msg_for_mistral_ai, user_id=message.from_user.id, chat_type=message.chat.type, save_dialog=False)
        update_last_search_time(message.from_user.id, int(time.time()))

@router.message(Command('stats'))
async def stats(message: Message):
    if await check_user_status(message):
        return
    if message.from_user.id != 905207082:
        return
    stats = get_stats()
    limits_message = "\n".join([f"{key}: {value}" for key, value in stats['limits'].items()])
    stats_message = (
        f"Total users: {stats['total_users']}\n"
        f"Frozen users: {stats['frozen_users']}\n"
        f"Processed users: {stats['processing_users']}\n"
        f"Sub users: {stats['paying_users']}\n\n"
        f"Limits:\n{limits_message}"
    )
    await message.reply(stats_message)

@router.message(Command('msg'))
async def mass_message(message: Message):
    if await check_user_status(message):
        return
    if message.from_user.id != 905207082:
        return
    stats = get_stats()
    user_ids = stats['user_ids']
    text = message.text.replace('/msg', '').strip()
    if not text:
        await message.reply("Incorrect use /msg")
        return
    i = 0
    for user_id in user_ids:
        try:
            await message.bot.send_message(chat_id=user_id, text=text)
            i += 1
        except Exception as e:
            print(f"Ошибка отправки пользователю {user_id}: {e}")

    await message.reply(f'Сообщения отправлены {i} пользователям.')

@router.message(Command('lang'))
async def change_lang(message: Message, state: FSMContext):
    if await check_user_status(message):
        return
    await state.update_data(uid=message.from_user.id)
    await message.reply('Select your language...', reply_markup=KeyBoard.lang_kb, parse_mode='Markdown')
    await state.set_state(Promt.lang_choose)

@router.message(Command('config'))
async def config(message: Message, state: FSMContext):
    if await check_user_status(message):
        return
    user_lang = user_get_lang(message.from_user.id)
    await state.update_data(uid=message.from_user.id, user_lang=user_lang)
    img_model, txt_model = user_get_config(message.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.button(text=translation(user_lang, "image_generation_model"), callback_data='IGM')
    builder.button(text=translation(user_lang, "text_generation_model"), callback_data='TGM')
    markup = builder.as_markup()
    await message.reply(translation(user_lang, "config_menu").format(img_model=img_model.split('/')[1], txt_model=txt_model), reply_markup=markup)
    await state.set_state(Promt.config_wait)

@router.message(Command('vision'))
async def img_for_text(message: Message, state: FSMContext):
    if await check_user_status(message, limit=('vision_limit', 1000), subscription_limit=1000):
        return
    await state.set_state(Promt.mistral_vision)
    user_lang = user_get_lang(message.from_user.id)
    await state.update_data(processing=message.from_user.id, user_lang=user_lang)
    await message.reply(translation(user_lang, "send_image"), parse_mode='Markdown')

@router.message(Command('image'))
async def promt_for_pic(message: Message, state: FSMContext):
    if await check_user_status(message, limit=('image_limit', 1000), subscription_limit=1000):
        return
    user_lang = user_get_lang(message.from_user.id)
    await state.update_data(processing=message.from_user.id, user_lang=user_lang)
    await state.set_state(Promt.image1)
    await message.reply(translation(user_lang, "enter_prompt"), parse_mode='Markdown')

@router.message(Command('image2'))
async def promt_for_pic(message: Message, state: FSMContext):
    if await check_user_status(message, limit=('image2_limit', 1000), subscription_limit=1000):
        return
    user_lang = user_get_lang(message.from_user.id)
    await state.set_state(Promt.bria_image_generation)
    await state.update_data(processing=message.from_user.id, user_lang=user_lang)
    await message.reply(translation(user_lang, "enter_prompt"), parse_mode='Markdown')

@router.message(Command('upscale'))
async def upscale_pic(message: Message, state: FSMContext):
    if await check_user_status(message, limit=('upscale_limit', 1000), subscription_limit=1000):
        return
    user_lang = user_get_lang(message.from_user.id)
    await state.set_state(Promt.bria_image_upscale)
    await state.update_data(processing=message.from_user.id, user_lang=user_lang)
    await message.reply(translation(user_lang, "send_image"), parse_mode='Markdown')

@router.message(Command('background'))
async def background_command_start(message: Message, state: FSMContext):
    if await check_user_status(message, limit=('background_limit', 1000), subscription_limit=1000):
        return
    user_lang = user_get_lang(message.from_user.id)
    await state.set_state(Promt.bria_background_prompt)
    await state.update_data(processing=message.from_user.id, user_lang=user_lang)
    await message.reply(translation(user_lang, "enter_prompt_background"), parse_mode='Markdown')

@router.message(Command('reimage'))
async def reimage_command_start(message: Message, state: FSMContext):
    if await check_user_status(message, limit=('reimage_limit', 1000), subscription_limit=1000):
        return
    user_lang = user_get_lang(message.from_user.id)
    await state.set_state(Promt.bria_reimage_prompt)
    await state.update_data(processing=message.from_user.id, user_lang=user_lang)
    await message.reply(translation(user_lang, "enter_prompt_reference"), parse_mode='Markdown')

@router.message(Command('expand'))
async def image_to_expand(message: Message, state: FSMContext):
    if await check_user_status(message, limit=('expand_limit', 1000), subscription_limit=1000):
        return
    user_lang = user_get_lang(message.from_user.id)
    await state.set_state(Promt.bria_expand)
    await state.update_data(processing=message.from_user.id, user_lang=user_lang)
    await message.reply(translation(user_lang, "send_image"), parse_mode='Markdown')

@router.callback_query(Promt.lang_choose)
async def language_choose(callback: CallbackQuery, state: FSMContext):
    user_id = await state.get_data()
    if user_id['uid'] == callback.from_user.id:
        await callback.answer('')
        await callback.message.edit_text(translation(callback.data, "switch_lang"))
        user_set_lang(callback.from_user.id, callback.data)

@router.message(Promt.bria_expand)
async def expanded_image(message: Message, state: FSMContext):
    state_data = await state.get_data()
    user_lang = state_data['user_lang']
    with_message=False
    if 'processing' in state_data:
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=False, image=True, with_message=with_message, user_lang=user_lang):
        return
    reply_message = await message.reply(translation(user_lang, "expanding"), parse_mode='Markdown')
    set_processing(message.from_user.id)
    file = await message.bot.get_file(file_id=message.photo[-1].file_id)
    image_url = f'https://api.telegram.org/file/bot{TOKEN}/{file.file_path}'
    await main_bria_image_expand(message=message, reply_message=reply_message, image_url=image_url)
    await state.clear()

@router.message(Promt.bria_background_prompt)
async def handle_bg_prompt(message: Message, state: FSMContext):
    state_data = await state.get_data()
    with_message=False
    if 'processing' in state_data:
        user_lang = state_data['user_lang']
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=True, image=False, with_message=with_message, user_lang=user_lang):
        return
    await state.update_data(processing=message.from_user.id, prompt=message.text, user_lang=user_lang)
    await state.set_state(Promt.bria_background)
    await message.reply(translation(user_lang, "send_image"), parse_mode='Markdown')

@router.message(Promt.bria_reimage_prompt)
async def handle_reimg_prompt(message: Message, state: FSMContext):
    state_data = await state.get_data()
    with_message=False
    user_lang = state_data['user_lang']
    if 'processing' in state_data:
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=True, image=False, with_message=with_message, user_lang=user_lang):
        return
    await state.update_data(processing=message.from_user.id, prompt=message.text, user_lang=user_lang)
    await state.set_state(Promt.bria_reimage)
    await message.reply(translation(user_lang, "send_image"), parse_mode='Markdown')

@router.message(Promt.bria_reimage)
async def start_generation_reimage(message: Message, state: FSMContext):
    state_data = await state.get_data()
    prompt = state_data['prompt']
    user_lang = state_data['user_lang']
    with_message=False
    if 'processing' in state_data:
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=False, image=True, with_message=with_message, user_lang=user_lang):
        return
    reply_message = await message.reply(translation(user_lang, "generating"), parse_mode='Markdown')
    set_processing(message.from_user.id)
    file = await message.bot.get_file(file_id=message.photo[-1].file_id)
    image_url = f'https://api.telegram.org/file/bot{TOKEN}/{file.file_path}'
    await main_bria_reimage(message=message, reply_message=reply_message, image_url=image_url, prompt=prompt)
    await state.clear()

@router.message(Promt.bria_background)
async def start_generation_background(message: Message, state: FSMContext):
    state_data = await state.get_data()
    prompt = state_data['prompt']
    user_lang = state_data['user_lang']
    with_message=False
    if 'processing' in state_data:
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=False, image=True, with_message=with_message, user_lang=user_lang):
        return
    reply_message = await message.reply(translation(user_lang, "generating"), parse_mode='Markdown')
    set_processing(message.from_user.id)
    file = await message.bot.get_file(file_id=message.photo[-1].file_id)
    image_url = f'https://api.telegram.org/file/bot{TOKEN}/{file.file_path}'
    await main_bria_background_change(message=message, reply_message=reply_message, image_url=image_url, prompt=prompt)
    await state.clear()

@router.message(Promt.bria_image_upscale)
async def upscale_image(message: Message, state: FSMContext):
    state_data = await state.get_data()
    with_message=False
    if 'processing' in state_data:
        user_lang = state_data['user_lang']
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=False, image=True, with_message=with_message, user_lang=user_lang):
        return
    reply_message = await message.reply(translation(user_lang, "analyzing_image"), parse_mode='Markdown')
    set_processing(message.from_user.id)
    file = await message.bot.get_file(file_id=message.photo[-1].file_id)
    image_url = f'https://api.telegram.org/file/bot{TOKEN}/{file.file_path}'
    await main_bria_upscaling(message=message, reply_message=reply_message, image_url=image_url)
    await state.clear()

@router.message(Promt.bria_image_generation)
async def start_generation(message: Message, state: FSMContext):
    state_data = await state.get_data()
    with_message=False
    if 'processing' in state_data:
        user_lang = state_data['user_lang']
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=True, image=False, with_message=with_message, user_lang=user_lang):
        return
    reply_message = await message.reply(translation(user_lang, "generating"), parse_mode='Markdown')
    set_processing(message.from_user.id)
    await main_bria_generation(message=message, reply_message=reply_message, user_text=message.text)
    await state.clear()


@router.message(Promt.mistral_vision)
async def img_for_text(message: Message, state: FSMContext):
    state_data = await state.get_data()
    with_message=False
    if 'processing' in state_data:
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=False, image=True, with_message=with_message, user_lang=state_data['user_lang']):
        return
    reply_message = await message.reply(translation(state_data['user_lang'], "analyzing_image"), parse_mode='Markdown')
    set_processing(message.from_user.id)
    file = await message.bot.get_file(file_id=message.photo[-1].file_id)
    image_url = f'https://api.telegram.org/file/bot{TOKEN}/{file.file_path}'
    await image_vision(message=message, reply_message=reply_message, model="pixtral-large-latest", image_url=image_url, user_id=message.from_user.id, user_lang=state_data['user_lang'])
    await state.clear()

@router.callback_query(Promt.config_wait)
async def config_wait(callback: CallbackQuery, state: FSMContext):
    user_id = await state.get_data()
    if user_id['uid'] == callback.from_user.id:
        if callback.data == 'IGM':
            await callback.message.edit_text('Choice model for image generation:', reply_markup=KeyBoard.inline_models)
            await state.set_state(Promt.config_set)
            await state.update_data(config=callback.data)
        elif callback.data == 'TGM':
            await callback.message.edit_text('Choice model for text generation:', reply_markup=KeyBoard.text_model)
            await state.set_state(Promt.config_set)
            await state.update_data(config=callback.data)

@router.callback_query(Promt.config_set)
async def config_set(callback: CallbackQuery, state: FSMContext):
    config_data = await state.get_data()
    await callback.answer('')
    user_set_config(callback.from_user.id, config_data['config'], callback.data)
    await callback.message.edit_text(translation(config_data['user_lang'], "config_success"))

@router.message(Promt.image1)
async def start_generation(message: Message, state: FSMContext):
    state_data = await state.get_data()
    with_message=False
    if 'processing' in state_data:
        user_id = state_data['processing']
        user_lang = state_data['user_lang']
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=True, image=False, with_message=with_message, user_lang=user_lang):
        return
    await state.update_data(uid=message.from_user.id)
    if user_id == message.from_user.id:
        end_text = GoogleTranslator(target='en').translate(message.text)
        await state.set_state(Promt.image1_final)
        img_model, txt_model = user_get_config(message.from_user.id)
        await state.update_data(promt=end_text, second_prompt=message.text, model=img_model, user_lang=user_lang)
        await message.reply(text=translation(user_lang, "choice_number"), reply_markup=KeyBoard.Generation_numbers, parse_mode='Markdown')

@router.callback_query(Promt.image1_num_images)
async def gen_numbers(callback: CallbackQuery, state: FSMContext):
    user_id = await state.get_data()
    if user_id['uid'] == callback.from_user.id:
        await state.update_data(model=callback.data)
        #if callback.data in HF_SUBSCRIPTION_MODELS and not has_subscription(callback.from_user.id):
            #await callback.answer('')
            #await callback.message.edit_text(text=f"Model *{callback.data.split('/')[1]}* is available by subscription only", parse_mode='Markdown')
            #await state.clear()
            #return
        await state.set_state(Promt.image1_final)
        await callback.answer('')
        await callback.message.edit_text(text=translation(user_id['user_lang'], "choice_number"), reply_markup=KeyBoard.Generation_numbers, parse_mode='Markdown')

@router.callback_query(Promt.image1_final)
async def finaly_generation(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data['uid'] == callback.from_user.id:
        num_gen = int(callback.data)
        #chat_type = callback.message.chat.type
        #if chat_type != 'private' and num_gen > 8:
            #num_gen = 8
        #if not has_subscription(data['uid']) and num_gen >= 5:
            #await callback.message.edit_text("You can only generate up to *4* images. To generate up to *10* images, *buy a subscription*", parse_mode='Markdown')
            #await state.clear()
            #return
        set_processing(callback.from_user.id)
        await callback.answer('')
        await callback.message.edit_text(translation(data['user_lang'], "generating"), parse_mode='Markdown')
        await main_image_generator(callback=callback, data=data, num_gen=num_gen)
        await state.clear()