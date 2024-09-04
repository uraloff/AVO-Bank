import logging
import asyncio
from os import getenv
from dotenv import load_dotenv

from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from App.Handlers.handlers import user_router
from App.Handlers.uz_handlers import uz_user_router
from App.Handlers.ru_handlers import ru_user_router


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s — %(name)s — %(levelname)s — %(message)s'
)


async def main():
    load_dotenv()

    logging.info("Загрузка конфигурации...")

    bot = Bot(
        token=getenv('TOKEN'),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    dp.include_routers(user_router, uz_user_router, ru_user_router)

    logging.info("Бот успешно запущен ✅")

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Бот успешно выключен ❌")