import os
import itertools
import httpx
from aiogram.types import Message, InputMediaPhoto
from deep_translator import GoogleTranslator
from snap_utils.database import clear_processing, increment_limit

BRIA_TOKENS = os.getenv('BRIA_TOKENS').split(',')
token_iterator_bria = itertools.cycle(BRIA_TOKENS)

async def start_bria_reimage(image_url: str, prompt: str):
    translated_text = GoogleTranslator(target='en').translate(prompt)
    BRIA_TOKEN = next(token_iterator_bria)
    url = "https://engine.prod.bria-api.com/v1/reimagine"
    payload = {"prompt": translated_text, "num_results": 4, "sync": True, "structure_image_url": image_url, "structure_ref_influence": 0.7, "fast": False}
    headers = {"Content-Type": "application/json", "api_token": BRIA_TOKEN}
    async with httpx.AsyncClient(timeout=300) as client:
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_err:
            if http_err.response.status_code == 400:
                return {"error": "Uncorrect text."}
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}
        
async def main_bria_reimage(message: Message, reply_message: Message, image_url: str, prompt: str):
    try:
        data = await start_bria_reimage(image_url, prompt)
        if 'error' in data:
            await reply_message.delete()
            await message.reply(data['error'])
        elif 'result' in data and isinstance(data['result'], list):
            files = [InputMediaPhoto(type='photo', media=item['urls'][0]) for item in data['result'] if 'urls' in item and item['urls']]
            if files:
                await reply_message.delete()
                await message.reply_media_group(media=files)
                increment_limit(message.from_user.id, 'reimage_limit', 4)
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