from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from handlers.register import FSMContext
from states.register import Register, Edit
from storage import load_data, save_data
from keyboards.inline import back_kb, edit_kb
from keyboards.inline import front_kb, back_edit
from keyboards.inline import profile_kb1, profile_kb2

router = Router()

@router.callback_query(F.data == 'profile')
async def handle_profile(callback: CallbackQuery):
    
    user_id = str(callback.from_user.id)
    users_data = load_data()
    profile = users_data.get(user_id)
    
    if profile is None:
        await callback.message.edit_text(
            "You have not registered yet!",
            reply_markup=profile_kb1
            )
        await callback.answer()
        return

    await callback.message.edit_text(
        "USER DATA"
        f"\nYour ID: {user_id}"
        f"\nYour name: {profile['name']}"
        f"\nYour age: {profile['age']}"
        f"\nYour favourite game: {profile['game']}",
        reply_markup=profile_kb2
        )
    await callback.answer()

@router.callback_query(F.data == 'edit')
async def handle_profile_edit(
    callback: CallbackQuery,
    ):
    await callback.message.edit_text(
        "What do you want to change from there?\n",
        reply_markup=edit_kb
        )
    await callback.answer()

@router.callback_query(F.data == 'edit_name')
async def handle_name_edit(
    callback: CallbackQuery,
    state: FSMContext
    ):
    await state.set_state(Edit.name)
    await callback.message.edit_text(
        "Change your name: ",
        reply_markup=back_edit
        )
    await callback.answer()

@router.callback_query(F.data == 'edit_age')
async def handle_name_edit(
    callback: CallbackQuery,
    state: FSMContext
    ):
    await state.set_state(Edit.age)
    await callback.message.edit_text(
        "Change your age: ",
        reply_markup=back_edit
        )
    await callback.answer()

@router.callback_query(F.data == 'edit_game')
async def handle_name_edit(
    callback: CallbackQuery,
    state: FSMContext
    ):
    await state.set_state(Edit.game)
    await callback.message.edit_text(
        "Change your game: ",
        reply_markup=back_edit
        )
    await callback.answer()

@router.callback_query(F.data == 'back_edit')
async def handle_start(
    callback: CallbackQuery,
    state: FSMContext
    ):
    await state.clear()
    await callback.message.edit_text(
        "Welcome Fren\nLet's register yourself together here!",
        reply_markup=edit_kb
        )
    await callback.answer()

@router.callback_query(F.data == 'del_profile')
async def handle_profile_button(
    callback: CallbackQuery
    ):
    user_id = str(callback.from_user.id)
    user_data = load_data()
    if user_id in user_data:
        del user_data[user_id]
    save_data(user_data)
    await callback.message.edit_text(
        "Profile deleted successfully",
        reply_markup=back_kb
        )
    

@router.message(Edit.name)
async def handle_edit_nameState(
    message: Message,
    state: FSMContext
    ):
    await state.clear()
    user_id = str(message.from_user.id)
    data = load_data()
    profile = data[user_id]
    profile['name'] = message.text
    save_data(data)
    await message.answer(
        "Name changed successfully",
        reply_markup=back_kb)

@router.message(Edit.age)
async def handle_edit_nameState(
    message: Message,
    state: FSMContext
    ):
    await state.clear()
    user_id = str(message.from_user.id)
    data = load_data()
    profile = data[user_id]
    profile['age'] = message.text
    save_data(data)
    await message.answer(
        "Age changed successfully",
        reply_markup=back_kb)

@router.message(Edit.game)
async def handle_edit_nameState(
    message: Message,
    state: FSMContext
    ):
    await state.clear()
    user_id = str(message.from_user.id)
    data = load_data()
    profile = data[user_id]
    profile['game'] = message.text
    save_data(data)
    await message.answer(
        "Game changed successfully",
        reply_markup=back_kb)