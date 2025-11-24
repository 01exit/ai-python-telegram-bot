import httpx
import random
from aiogram.types import Message, BufferedInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw
from io import BytesIO
from collections import Counter

COLOR_EMOJIS = {
    "red": "🟥",
    "green": "🟩",
    "blue": "🟦",
    "yellow": "🟨",
    "purple": "🟪",
    "orange": "🟧",
    "white": "⬜",
    "black": "⬛",
    "gray": "🔲"
}

def get_closest_color(r, g, b):
    # Базовые цвета и их RGB
    base_colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "purple": (128, 0, 128),
        "orange": (255, 165, 0),
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "gray": (128, 128, 128)
    }

    # Рассчитываем расстояние до каждого цвета
    closest_color = min(base_colors, key=lambda color: 
                        (r - base_colors[color][0]) ** 2 + 
                        (g - base_colors[color][1]) ** 2 + 
                        (b - base_colors[color][2]) ** 2)
    return closest_color

def generate_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def generate_inline_buttons(objects, color_map):

    # Группируем объекты по label и считаем их количество
    labels_count = Counter(obj['label'] for obj in objects)
    buttons = []

    # Создаём кнопки для каждого label
    for label, count in labels_count.items():
        # Используем первый найденный цвет из color_map для этого label
        object_indices = [i for i, obj in enumerate(objects) if obj['label'] == label]
        first_object_index = object_indices[0]
        color_name = get_closest_color(*color_map[first_object_index][:3])
        emoji = COLOR_EMOJIS.get(color_name, "⬜")  # Эмодзи цвета
        button_text = f"{emoji} {label} ({count})"  # Текст кнопки
        buttons.append(InlineKeyboardButton(text=button_text, callback_data=f"label:{label}"))

    # Создаём InlineKeyboardMarkup с кнопками
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons[i:i+2] for i in range(0, len(buttons), 2)])
    return keyboard

async def get_objects(image_url: str):
    API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
    headers = {"Authorization": "Bearer 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"}
    async with httpx.AsyncClient(timeout=300) as client:
        try:
            response = await client.post(API_URL, headers=headers, data=image_url)
            image_data = await client.get(image_url)
            return response.json(), BytesIO(image_data.content)
        except httpx.HTTPStatusError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        
async def start_visual_image_with_objects(image_data, objects):
    img = Image.open(image_data).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    color_map = {}

    for idx, obj in enumerate(objects):
        box = obj['box']
        rect = (box['xmin'], box['ymin'], box['xmax'], box['ymax'])
        # Генерируем цвет для каждого объекта
        color = generate_random_color() + (50,)
        color_map[idx] = color  # Сохраняем цвет по индексу объекта
        outline_color = color[:3]  # Контур без прозрачности
        draw.rectangle(
            rect,
            fill=color,
            outline=outline_color,
            width=3
        )

    img = Image.alpha_composite(img, overlay)
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='png')
    img_byte_arr.seek(0)
    return img_byte_arr, color_map  # Возвращаем изображение и цветовую карту


async def visual_mask(message: Message, image_url: str):
    try:
        objects, image_data = await get_objects(image_url)
        if 'error' in objects:
            await message.reply(objects['error'])
        elif not objects:
            await message.reply('No objects found')
        else:
            visual_mask, color_map = await start_visual_image_with_objects(image_data, objects)
            visual_mask.seek(0)
            photo = BufferedInputFile(visual_mask.read(), filename="visual_mask.jpg")
            keyboard = generate_inline_buttons(objects, color_map)
            await message.answer_photo(photo=photo, reply_markup=keyboard)
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

def generate_mask():
    pass