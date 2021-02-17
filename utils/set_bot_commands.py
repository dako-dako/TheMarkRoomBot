from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("/start", "Start"),
        types.BotCommand("/help", "Help"),
        types.BotCommand("/feedback", "Feedback"),
        types.BotCommand("/menu", "More Functions"),
        types.BotCommand("/videos", "Videos"),
        types.BotCommand("/faq", "FAQ")
    ])