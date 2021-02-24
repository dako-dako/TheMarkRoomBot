import asyncio

from data import config
from utils.dp_api import quick_commands
from utils.dp_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем пользователей")
    await quick_commands.add_user(1, "Danila", "Koshevoi", "danilaitkoshevoi@gmail.com", "Arrived", "306")
    await quick_commands.add_user(2, "Vlad", "Nechaev", "vladnechaev@gmail.com", "Not Arrived", "500")
    await quick_commands.add_user(3, "Masha", "Baranova", "masha@gmail.com", "Arrived", "200")
    await quick_commands.add_user(4, "Polina", "Cihanova", "polina@gmail.com", "Not Arrived", "104")
    await quick_commands.add_user(5, "Ismail", "Guseinov", "ismail@gmail.com", "Arrived", "102")

    print("Готово")

    users = await quick_commands.select_all_users()
    print(f"Получил всех пользователей: {users}")

    count_users = await quick_commands.count_users()
    print(f"Всего пользователей: {count_users}")

    user = await quick_commands.select_user(id=5)
    print(f"Получил пользователя: {user}")

loop = asyncio.get_event_loop()
loop.run_until_complete(test())