from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp



@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List of available commands: ",
            "/start - Start conversation",
            "/help - List of available commands",
            "/feedback - Give your feedback",
            "/menu - More functions",
            "/videos - List of available videos",
            "/faq - Frequently Asked Questions")

    await message.answer("\n".join(text))
