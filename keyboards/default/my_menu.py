from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    row_width=2,
    keyboard = [
        [
            KeyboardButton(text="🔑Register🔑"),
            KeyboardButton(text="📱Contacts📱"),
        ],
        [
            KeyboardButton(text="🎞Videos🎞"),
            KeyboardButton(text="ℹ️FAQℹ️"),
        ],
        [
            KeyboardButton(text="😊Feedback😊"),
            KeyboardButton(text="😱Complain😱"),
        ],
    ],
    resize_keyboard=True
)