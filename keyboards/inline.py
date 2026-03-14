from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

front_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Register",
            callback_data='register'
            )],
        [InlineKeyboardButton(
            text="Profile",
            callback_data='profile'
            )]
        ]
    )

edit_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Name",
            callback_data='edit_name'
            )],
        [InlineKeyboardButton(
            text="Age",
            callback_data='edit_age'
            )],
        [InlineKeyboardButton(
            text="Game",
            callback_data='edit_game'
            )],
        [InlineKeyboardButton(
            text="Back",
            callback_data='back'
            )]
        ]
    )

back_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Back",
            callback_data='back'
            )]
        ]
    )

back_edit = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Back",
            callback_data='back_edit'
            )]
        ]
    )

profile_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Register",
            callback_data='register'
            )],
        [InlineKeyboardButton(
            text="Back",
            callback_data='back'
            )]
        ]
    )

profile_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Back",
            callback_data='back'
            )],
        [InlineKeyboardButton(
            text="Edit Profile",
            callback_data='edit'
            )],
        [InlineKeyboardButton(
            text="Delete Profile",
            callback_data='del_profile',
            style="danger"
            )]
        ]
    )

terminate_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Terminate",
            callback_data='terminate'
            )]
        ]
    )
