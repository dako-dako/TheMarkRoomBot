from aiogram.dispatcher.filters.state import StatesGroup, State


class Survey(StatesGroup):
    Q1 = State()
    Q2 = State()