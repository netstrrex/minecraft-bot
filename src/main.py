import asyncio

from aiogram import Bot, Dispatcher

from core.settings import settings
from telegram_bot.handlers import router

bot = Bot(settings.bot.token)
dp = Dispatcher()
dp.include_router(router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
