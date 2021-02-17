from aiogram.dispatcher.filters.state import StatesGroup, State

class RegistrationProcess(StatesGroup):
    NotApprovedResident = State()
    ApprovedResident = State()
    FirstName = State()
    LastName = State()
    Email = State()
    ArrivalStatus = State()
    RoomNumber = State()
    RegisteredPerson = State()