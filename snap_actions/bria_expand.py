import os
import itertools
import httpx
from aiogram.types import Message
from snap_utils.database import clear_processing, increment_limit

BRIA_TOKENS = os.getenv('BRIA_TOKENS').split(',')
token_iterator_bria = itertools.cycle(BRIA_TOKENS)

async def start_bria_image_expand(image_url: str, width: int, height: int):
    BRIA_TOKEN = next(token_iterator_bria)
    max_size = 5000
    increase = 500
    target_width = min(width + increase, max_size)
    target_height = min(height + increase, max_size)
    original_x = (target_width - width) // 2
    original_y = (target_height - height) // 2
    canvas_area = target_width * target_height
    original_area = width * height
    if original_area <= 0.15 * canvas_area:
        return {"error": "Original image area must be more than 15% of the canvas area."}
    url =  "https://engine.prod.bria-api.com/v1/image_expansion"
    payload = {
        "image_url": image_url,
        "canvas_size": [target_width, target_height],
        "original_image_size": [width, height],
        "original_image_location": [original_x, original_y]
    }
    headers = {"Content-Type": "application/json", "api_token": BRIA_TOKEN}
    async with httpx.AsyncClient(timeout=300) as client:
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_err:
            if http_err.response.status_code == 406:
                return {"error": "Minimum resolution supported for width and/or height is 216 pixels."}
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}
    
async def main_bria_image_expand(message: Message, reply_message: Message, image_url: str):
    try:
        data = await start_bria_image_expand(image_url, message.photo[-1].width, message.photo[-1].height)
        if 'error' in data:
            await reply_message.delete()
            await message.reply(data['error'])
        elif 'result_url' in data:
            result_url = data['result_url']
            if result_url:
                await reply_message.delete()
                await message.reply_photo(result_url)
                increment_limit(message.from_user.id, 'expand_limit', 1)
            else:
                await reply_message.delete()
                await message.reply("No valid images to send. Please try again.")
        else:
            await reply_message.delete()
            await message.reply("No images found in the response.")
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
    finally:
        clear_processing(message.from_user.id)