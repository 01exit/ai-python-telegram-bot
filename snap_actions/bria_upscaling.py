import os
import itertools
import httpx
import aiohttp
import tempfile
from aiogram.types import Message, FSInputFile
from snap_utils.database import clear_processing, increment_limit

BRIA_TOKENS = os.getenv('BRIA_TOKENS').split(',')
token_iterator_bria = itertools.cycle(BRIA_TOKENS)

async def start_bria_upscaling(image_url: str):
    BRIA_TOKEN = next(token_iterator_bria)
    url = "https://engine.prod.bria-api.com/v1/image/increase_resolution"
    query = {"desired_increase": "4"}
    payload = {"image_url": image_url}
    headers = {"Content-Type": "application/x-www-form-urlencoded", "api_token": BRIA_TOKEN}
    async with httpx.AsyncClient(timeout=300) as client:
        try:
            response = await client.post(url, data=payload, headers=headers, params=query)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_err:
            if http_err.response.status_code == 406:
                return {"error": "Minimum resolution supported for width and/or height is 216 pixels."}
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

async def main_bria_upscaling(message: Message, reply_message: Message, image_url: str):
    try:
        data = await start_bria_upscaling(image_url)
        if 'error' in data:
            await message.reply(data['error'])
            return
        elif 'result_url' in data:
            result_url = data['result_url']
            if result_url:
                async with aiohttp.ClientSession() as session:
                    async with session.get(result_url) as resp:
                        if resp.status == 200:
                            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                                temp_file.write(await resp.read())
                                temp_file_path = temp_file.name
                            doc_file = FSInputFile(path=temp_file_path)
                            await reply_message.delete()
                            await message.reply_document(document=doc_file)
                            increment_limit(message.from_user.id, 'upscale_limit', 1)
                            os.remove(temp_file_path)
            else:
                await reply_message.delete()
                await message.reply("Failed to retrieve the upscaled image URL.")
        else:
            await reply_message.delete()
            await message.reply("No images found in the response.")
    except Exception as e:
        await reply_message.delete()
        await message.reply(text=str(e))
    finally:
        clear_processing(message.from_user.id)