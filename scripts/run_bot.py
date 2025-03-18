import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bot.bot_handlers import router # Импортируем router из bot/
# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

async def start_polling():
    # Загружаем переменные окружения
    load_dotenv()

    # Получаем токен бота
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN не найден в .env файле")
        sys.exit(1)

    # Создаём бота и диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot=bot)

    # Подключаем обработчики
    dp.include_router(router)

    logger.info("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_polling())

