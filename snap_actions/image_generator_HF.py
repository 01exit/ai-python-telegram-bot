import os
import itertools
import httpx
import time
import asyncio
from aiogram.types import BufferedInputFile, InputMediaPhoto, CallbackQuery
from aiogram.exceptions import TelegramBadRequest, TelegramRetryAfter
from snap_utils.database import clear_processing, increment_limit

HF_TOKEN_SET = os.getenv('HF_TOKEN_SET').split(',')
token_iterator = itertools.cycle(HF_TOKEN_SET)

async def img_sending(data):
    HF_TOKEN = next(token_iterator)
    headers = {"authorization": f"Bearer {HF_TOKEN}", "x-use-cache": "False"}
    API_URL = f"https://api-inference.huggingface.co/models/{data['model']}"
    async with httpx.AsyncClient(timeout=600) as client:
        for attempt in range(3):
            try:
                response = await client.post(API_URL, headers=headers, json={
                    "inputs": data['promt']
                })
                if response.status_code == 200:
                    file = BufferedInputFile(response.content, filename="image.jpg")
                    return InputMediaPhoto(type='photo', media=file)
            except httpx.ReadTimeout:
                return None
    return None

async def send_media_group(callback, files):
    chunk_size = 5
    for i in range(0, len(files), chunk_size):
        chunk = files[i:i + chunk_size]
        try:
            await callback.message.reply_media_group(media=chunk)
            await asyncio.sleep(1)  # Добавляем задержку между отправками
        except TelegramBadRequest as e:
            await callback.message.reply(f"{e}")
        except TelegramRetryAfter as e:
            await callback.message.reply(f"{e}")

async def main_image_generator(callback: CallbackQuery, data: dict, num_gen: int):
    start_time = time.time()
    increment_limit(callback.from_user.id, 'image_limit', num_gen)
    files = []
    try:
        tasks = [img_sending(data) for _ in range(num_gen)]
        results = await asyncio.gather(*tasks)
        for result in results:
            if result is not None:
                files.append(result)

        if not files:
            await callback.message.edit_text("No images were generated. Please try again.")
        else:
            end_time = time.time()
            generation_time = int(end_time - start_time)
            await callback.message.edit_text(
                f"Text: {data['second_prompt']}\n"
                f"Model: {data['model'].split('/')[1]}\n"
                f"Generation time: {generation_time} seconds",
                parse_mode=None
            )
            await send_media_group(callback, files)
    except TelegramBadRequest as e:
        await callback.message.reply(f"{e}")
    except TelegramRetryAfter as e:
        await callback.message.reply(f"{e}")
    finally:
        clear_processing(callback.from_user.id)
