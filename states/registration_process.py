from aiogram.dispatcher.filters.state import StatesGroup, State

class RegistrationProcess(StatesGroup):
    FullName = State()