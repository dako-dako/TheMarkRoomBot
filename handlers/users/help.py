from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List of available commands: ",
            "/start - Start conversation",
            "/help - List of available commands",
            "/info - Information about this bot",
            "/feedback - Give your feedback",
            "/menu - More functions")

    await message.answer("\n".join(text))
