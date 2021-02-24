from asyncpg import UniqueViolationError

from utils.dp_api.db_gino import db
from utils.dp_api.schemas.user import User


async def add_user(id: int, name: str, last_name: str, email: str,
                   resident_arrival_status: str, room_number: str):
    try:
        user = User(id=id, name=name, last_name=last_name, email=email,
                   resident_arrival_status=resident_arrival_status,
                   room_number=room_number)

        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_resident_arrival_status(id, resident_arrival_status):
    user = await User.get(id)
    await user.update(resident_arrival_status=resident_arrival_status).apply()


