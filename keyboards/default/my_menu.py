from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    row_width=3,
    keyboard = [
        [
            KeyboardButton(text="ℹ️FAQℹ️"),
            KeyboardButton(text="🎞Videos🎞"),
            KeyboardButton(text="👮‍Complain👮‍")
        ],
        [
            KeyboardButton(text="✌️WhatsApp Group✌️"),
            KeyboardButton(text="📱Contacts📱"),
        ],
        [
            KeyboardButton(text="😊Feedback😊"),
            KeyboardButton(text="🛫Arrival Status🛫")
        ],
    ],
    resize_keyboard=True
)
