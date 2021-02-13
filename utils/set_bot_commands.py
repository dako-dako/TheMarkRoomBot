from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("/start", "Start conversation"),
        types.BotCommand("/help", "Help"),
        types.BotCommand("/info", "Bot's info"),
    ])