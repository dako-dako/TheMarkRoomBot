from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    row_width=2,
    keyboard = [
        [
            KeyboardButton(text="✌️WhatsApp Group✌️"),
            KeyboardButton(text="🎞Videos🎞"),
        ],
        [
            KeyboardButton(text="ℹ️FAQℹ️"),
            KeyboardButton(text="📱Contacts📱"),
        ],
        [
            KeyboardButton(text="😊Feedback😊"),
            KeyboardButton(text="🛫Arrival Status🛫")
        ],
    ],
    resize_keyboard=True
)
