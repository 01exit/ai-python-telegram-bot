import os
import itertools
import asyncio
from aiogram.types import Message
from mistralai import Mistral
from snap_utils.database import clear_processing, increment_limit
from snap_utils.utils import translation

MISTRAL_TOKENS = os.getenv('MISTRAL_TOKENS').split(',')
token_iterator_mistral = itertools.cycle(MISTRAL_TOKENS)

async def image_vision(message: Message, reply_message: Message, model: str, image_url: str, user_id: int, user_lang: str):
    MISTRAL_TOKEN = next(token_iterator_mistral)
    client = Mistral(api_key=MISTRAL_TOKEN)
    try:
        messages = [
            {"role": "user", "content": [{"type": "text", "text": message.caption or translation(user_lang, "whats_in_this_image")}, {"type": "image_url", "image_url": image_url}]}
        ]
        chat_response = await asyncio.to_thread(client.chat.complete, model=model, messages=messages)
        await reply_message.edit_text(text=chat_response.choices[0].message.content, parse_mode='Markdown')
        increment_limit(message.from_user.id, 'vision_limit', 1)
    except Exception as e:
        await reply_message.edit_text(text=str(e))
    finally:
        clear_processing(user_id)