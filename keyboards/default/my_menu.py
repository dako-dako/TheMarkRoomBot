from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🔑Register🔑")
        ],
        [
            KeyboardButton(text="📱Contacts📱"),
        ],
        [
            KeyboardButton(text="🏠Arrival status🏠"),
        ],
    ],
    resize_keyboard=True
)