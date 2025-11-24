import os
import itertools
import httpx
from aiogram.types import Message
from snap_utils.database import clear_processing, increment_limit

BRIA_TOKENS = os.getenv('BRIA_TOKENS').split(',')
token_iterator_bria = itertools.cycle(BRIA_TOKENS)

async def start_bria_inpaint(image_url: str, mask_url: str):
    BRIA_TOKEN = next(token_iterator_bria)
    url = "https://engine.prod.bria-api.com/v1/eraser"
    payload = {"image_url": image_url, "mask_url": mask_url}
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
        
async def main_bria_inpaint(message: Message, reply_message: Message, image_url: str, mask_url: str):
    try:
        data = await start_bria_inpaint(image_url, mask_url)
        if 'error' in data:
            await reply_message.delete()
            await message.reply(data['error'])
        elif 'result_url' in data:
            result_url = data['result_url']
            if result_url:
                await reply_message.delete()
                await message.reply_photo(result_url)
                increment_limit(message.from_user.id, 'inpaint_limit', 1)
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



'''
FOR HANDLERS

from bria_inpaint import main_bria_inpaint
from bria_inpaint_create_mask import visual_mask
from bria_inpaint_create_mask import generate_mask

    bria_inpaint_image = State()
    bria_impaint_mask = State()

@router.message(Command('inpaint'))
async def inpaint_image(message: Message, state: FSMContext):
    if await check_user_status(message, limit=('inpaint_limit', 20), subscription_limit=9960):
        return
    await state.set_state(Promt.bria_inpaint_image)
    await state.update_data(processing=message.from_user.id)
    await message.reply('*Send only 1 image*', parse_mode='Markdown')

@router.message(Promt.bria_inpaint_image)
async def bria_inpaint_visual_mask(message: Message, state: FSMContext):
    state_data = await state.get_data()
    with_message=False
    if 'processing' in state_data:
        await state.clear()
        with_message=True
    if await inputs_checker(message, text=False, image=True, with_message=with_message):
        return
    file = await message.bot.get_file(file_id=message.photo[-1].file_id)
    image_url = f'https://api.telegram.org/file/bot{TOKEN}/{file.file_path}'
    await visual_mask(message=message, image_url=image_url)
'''