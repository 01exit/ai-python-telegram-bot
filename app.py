import asyncio
import logging
import os
import sys
from dotenv import load_dotenv
from snap_utils.database import initialize_database, clear_all_processing, check_subscriptions, reset_limits, clear_dialog_history
from aiogram import Bot, Dispatcher
from handlers import router
from logging.handlers import RotatingFileHandler
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web

load_dotenv()
API_TOKEN = os.getenv('TOKEN')
WEBHOOK_URL = f"https://{os.getenv('HEROKU_APP_NAME')}.herokuapp.com/{API_TOKEN}"  # Heroku URL

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        RotatingFileHandler("bot.log", maxBytes=50000000, backupCount=5, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

async def run_check_subscriptions():
    await check_subscriptions()

async def run_reset_limits():
    await reset_limits()
    await clear_dialog_history()

async def on_startup():
    """Установка вебхука при старте"""
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown():
    """Удаление вебхука при завершении"""
    await bot.delete_webhook()

async def main():
    dp.include_router(router)
    await on_startup()
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=f"/{API_TOKEN}")
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 5000)))
    await site.start()

    try:
        while True:
            await asyncio.sleep(3600)  # Фоновая работа сервера
    except (KeyboardInterrupt, SystemExit):
        await on_shutdown()
        await runner.cleanup()

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == 'check_subscriptions':
                asyncio.run(run_check_subscriptions())
            elif sys.argv[1] == 'reset_limits':
                asyncio.run(run_reset_limits())
        else:
            initialize_database()
            clear_all_processing()
            logging.info("Bot is starting...")
            asyncio.run(main())
    except KeyboardInterrupt:
        logging.warning('Bot stopped by user (KeyboardInterrupt)')
