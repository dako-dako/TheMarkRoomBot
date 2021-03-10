from sqlalchemy import Column, BigInteger, String, sql

from utils.dp_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    resident_arrival_status = Column(String(100))
    room_number = Column(String(100))
    query: sql.Select