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

from fastapi import FastAPI, Request
import uvicorn
import requests
import os

WEBHOOK_PATH = f"/{TOKEN}"
app = FastAPI()

@app.post(WEBHOOK_PATH)
async def telegram_webhook(req: Request):
    update = await req.json()
    print(update)  # handle the update here
    return {"ok": True}

# optional: set webhook on start
def set_webhook():
    url = os.getenv("RAILWAY_STATIC_URL") + WEBHOOK_PATH
    requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={url}")
    
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    set_webhook()
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    asyncio.run(main())
