import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from App.Handlers.handlers import user_router
from App.Handlers.uz_handlers import uz_user_router
from App.Handlers.ru_handlers import ru_user_router


async def on_startup():
    print("Бот успешно запущен ✅")


async def main():
    load_dotenv()

    bot = Bot(
        token=getenv('TOKEN'),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.include_routers(user_router, uz_user_router, ru_user_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот успешно выключен ❌")