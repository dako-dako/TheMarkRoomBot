from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hey and Welcome, 😍{message.from_user.full_name}😍!\n\n"
                         f"Please type ❗️/info❗️ to move further!")
