import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.routers import main_router
from src.configs.app_config import app_settings


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Или logging.DEBUG
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


async def main():
    try:
        logger.info("Bot is starting...")

        bot = Bot(
            token=app_settings.BOT_TOKEN,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML)
        )

        dp = Dispatcher()
        dp.include_router(main_router)

        await bot.delete_webhook(drop_pending_updates=True)

        logger.info("Polling started.")
        await dp.start_polling(bot)

    except Exception as e:
        logger.exception("Unhandled exception occurred in main")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception("Unhandled exception occurred during bot startup")
        exit(1)
