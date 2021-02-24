from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_menu = ReplyKeyboardMarkup(
    row_width=1,
    keyboard=[
        [
            KeyboardButton(text="🔑Register🔑")
        ]
    ],
    resize_keyboard=True
)