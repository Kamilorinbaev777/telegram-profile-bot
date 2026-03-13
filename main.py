import asyncio
import os
from aiogram import Bot, Dispatcher

from handlers.start import router as start_router
from handlers.register import router as register_router
from handlers.profile import router as profile_router
from handlers.fallback import router as fallback_router
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(register_router)
dp.include_router(profile_router)
dp.include_router(fallback_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())