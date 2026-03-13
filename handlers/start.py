from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from handlers.profile import FSMContext
from keyboards.inline import front_kb

router = Router()

@router.message(CommandStart())
async def handle_starty(message: Message):
    await message.answer(
        "Welcome Fren\nLet's register yourself together here!",
        reply_markup=front_kb
        )

@router.callback_query(F.data == 'back')
async def handle_start(
    callback: CallbackQuery,
    ):
    await callback.message.edit_text(
        "Welcome Fren\nLet's register yourself together here!",
        reply_markup=front_kb
        )
    await callback.answer()