from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from storage import load_data, save_data
from keyboards.inline import back_kb, terminate_kb
from states.register import Register

router = Router()

@router.callback_query(F.data == 'terminate')
async def handle_terminate(
    callback: CallbackQuery,
    state: FSMContext
    ):
    await state.clear()
    await callback.message.edit_text(
        "Registration terminated!",
        reply_markup=back_kb)
    await callback.answer()    

@router.callback_query(F.data == 'register')
async def handle_register(
    callback: CallbackQuery,
    state: FSMContext
    ):
    await state.set_state(Register.name)
    await callback.message.edit_text(
        "What is your name?",
        reply_markup=terminate_kb
        )
    await callback.answer()

@router.message(Register.name)
async def handle_name_state(
    message: Message,
    state: FSMContext):

    user_name = str(message.text)

    if len(user_name) < 3 or len(user_name) > 10:
        await message.answer(
            "invalid name!"
            "\nName length must be between 3 and 10"
            )
        return

    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer(
        "How old are you?",
        reply_markup=terminate_kb
        )

@router.message(Register.age)
async def handle_age_state(
    message: Message,
    state: FSMContext):

    try:
        n = int(message.text)
    except ValueError:
        await message.answer(
            "Invalid age, age must be an integer!",
            reply_markup=terminate_kb                 
            )
        return

    if n < 0 or n > 120:
        await message.reply(
            "Invalid age, try sending an age that close to the realism",
            reply_markup=terminate_kb
            )
        return

    await state.update_data(age=n)
    await state.set_state(Register.game)
    await message.answer(
        "What's your favourite game?",
        reply_markup=terminate_kb
        )

@router.message(Register.game)
async def handle_contact_state(
    message: Message,
    state: FSMContext
    ):

    await state.update_data(game=message.text)
    await message.answer(
        "You completed registration process successfully",
        reply_markup=back_kb
        )

    user_id = str(message.from_user.id)
    users_data = load_data()
    data = await state.get_data()

    users_data[user_id] = {
        "name": data['name'],
        "age": data['age'],
        "game": data['game']
        }

    save_data(users_data)
    await state.clear()

