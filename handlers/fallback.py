from aiogram import Router, F
from aiogram.types import Message

from keyboards.inline import back_kb
router = Router()

#extra cases

@router.message(F.text == "developer")
async def handle_secret_text(message: Message):
    await message.answer(
        "Congrats you found a secret word hidden in this bot!",
        reply_markup=back_kb
        )

@router.message(F.sticker)
async def handle_sticker(message: Message):
    await message.answer("Nice sticker, fren")

@router.message(F.photo)
async def handle_sticker(message: Message):
    await message.answer("Nice photo, fren")

@router.message(F.document)
async def handle_document(message: Message):
    await message.answer("Nice doc, fren")

@router.message()
async def handle_fallback(message: Message):
    await message.answer(
        "There is no command for your request",
        reply_markup=back_kb
        )