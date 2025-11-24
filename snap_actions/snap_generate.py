import os
import itertools
import asyncio
import re
from aiogram.types import Message
from mistralai import Mistral
from snap_utils.database import clear_processing, increment_limit, save_dialog_message, get_dialog_history

MISTRAL_TOKENS = os.getenv('MISTRAL_TOKENS').split(',')
token_iterator_mistral = itertools.cycle(MISTRAL_TOKENS)

def escape_markdown(text: str):
    """
    Экранирует специальные символы Markdown (первая версия).
    """
    special_characters = r"_*[]()`"
    return re.sub(r"([%s])" % re.escape(special_characters), r"\\\1", text)

async def mistral_generate(reply_message: Message, model: str, user_text: str, user_id: int, chat_type: str, save_dialog: bool = True, hide: bool = False):
    MISTRAL_TOKEN = next(token_iterator_mistral)
    client = Mistral(api_key=MISTRAL_TOKEN)
    try:
        dialog_history = get_dialog_history(user_id)
        messages = [{"role": role, "content": message} for message, role in dialog_history]
        messages.append({"role": "user", "content": user_text})
        if chat_type != 'private':
            chat_response = await asyncio.wait_for(
                asyncio.to_thread(
                    client.chat.complete,
                    model=model,
                    messages=messages
                ),
                timeout=60
            )
            if not hide:
                increment_limit(user_id, 'snap_limit', 1)
                await reply_message.edit_text(chat_response.choices[0].message.content, parse_mode='Markdown')
            return chat_response.choices[0].message.content
        else:
            chat_response = await asyncio.wait_for(
                asyncio.to_thread(
                    client.chat.stream,
                    model=model,
                    messages=messages
                ),
                timeout=60
            )
            msg = ""
            previous_msg = ""
            buffer = ""  # Буфер для накопления текста
            update_threshold = 100  # Количество символов или слов для редактирования (настроить по необходимости)
            for chunk in chat_response:
                content = chunk.data.choices[0].delta.content
                if not content:
                    continue
                buffer += content
                if len(buffer) >= update_threshold or len(buffer.split()) >= update_threshold:
                    msg += buffer
                    buffer = ""
                    cleaned_msg = msg.strip()
                    escaped_msg = escape_markdown(cleaned_msg)
                    if escaped_msg == previous_msg:
                        continue
                    previous_msg = escaped_msg
                    try:
                        await reply_message.edit_text(escaped_msg, parse_mode='Markdown')
                    except Exception as e:
                        print(f"Ошибка при редактировании сообщения: {e}")
                        if "MESSAGE_TOO_LONG" in str(e):
                            break
                        try:
                            await reply_message.edit_text(cleaned_msg)
                        except Exception as fallback_error:
                            print(f"Ошибка при отправке текста без Markdown: {fallback_error}")
                            if "MESSAGE_TOO_LONG" in str(e):
                                break
            if not hide:
                increment_limit(user_id, 'snap_limit', 1)
            if buffer.strip():
                msg += buffer
                cleaned_msg = msg.strip()
                if cleaned_msg != previous_msg:
                    try:
                        if not hide:
                            await reply_message.edit_text(cleaned_msg, parse_mode='Markdown')
                    except Exception as e:
                        print(f"Ошибка при финальном редактировании: {e}")
                        try:
                            if not hide:
                                await reply_message.edit_text(cleaned_msg)
                        except Exception as fallback_error:
                            print(f"Ошибка при отправке текста без Markdown: {fallback_error}")
            return msg
    except asyncio.TimeoutError:
        await reply_message.edit_text(text="Request timed out. Please try again.")
    except Exception as e:
        await reply_message.edit_text(text=str(e))
    finally:
        clear_processing(user_id)
        if save_dialog:
            save_dialog_message(user_id, user_text, "user")
            if chat_type != 'private':
                save_dialog_message(user_id, chat_response.choices[0].message.content, "assistant")
            else:
                save_dialog_message(user_id, msg, "assistant")