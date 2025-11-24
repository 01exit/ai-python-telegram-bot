from aiogram.types import Message
from .utils import translation
from .database import (
    is_user_registered,
    is_user_frozen,
    is_processing,
    has_subscription,
    limit_reached,
    is_paying,
    user_get_lang
)

async def check_user_status(message: Message, check_payment: bool = False, limit: tuple = None, subscription_limit: int = None, query_check: bool = False):
    user_id = message.from_user.id
    if not is_user_registered(user_id):
        await message.answer('To use bot commands, register with the /reg command')
        return True
    if is_user_frozen(user_id):
        await message.answer("You have been blocked. Write to the user @wirex663 in private messages to unblock")
        return True
    if is_processing(user_id):
        user_lang = user_get_lang(user_id)
        await message.reply(translation(user_lang, "request_processing"))
        return True
    if check_payment and is_paying(user_id):
        user_lang = user_get_lang(user_id)
        await message.reply(translation(user_lang, "previous_donation_pending"))
        return True
    if limit:
        if has_subscription(user_id) and subscription_limit:
            max_limit = subscription_limit
        else:
            max_limit = limit[1]
        if limit_reached(user_id, limit[0], max_limit):
            await message.reply(translation(user_lang, "limit_reached").format(max_limit=max_limit))
            return True
    return False

async def inputs_checker(message: Message, text: bool, image: bool, with_message: bool = False, user_lang: str = "en"):
    if text:
        if not message.text:
            if with_message:
                await message.reply(translation(user_lang, "not_a_text"))
            return True
    if image:
        if not message.photo:
            if with_message:
                await message.reply(translation(user_lang, "not_an_image"))
            return True
        if message.media_group_id is not None:
            if with_message:
                await message.reply(translation(user_lang, "too_many_images"))
            return True
    return False