from utils.set_bot_commands import set_default_commands

from aiogram import executor

from loader import dp, db
from utils.dp_api import db_gino
from utils.notify_admins import on_startup_notify


async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)
    print("Connect DB")
    await db_gino.on_startup(dp)
    print("Ready")

    print("Clean DB")
    await db.gino.drop_all()

    print("Ready")

    print("Create tables")
    await db.gino.create_all()
    print("Ready")



if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)