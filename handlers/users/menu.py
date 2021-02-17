from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery


from keyboards.default import menu
from keyboards.inline.room_choice_buttons import room_choice
from keyboards.inline.arrival_choice_buttons import arrival_choice
from keyboards.inline.approval_choice_buttons import approval_choice
from keyboards.inline.room_callback_datas import choose_callback
from keyboards.inline.arrival_callback_datas import arrival_callback
from keyboards.inline.approval_callback_datas import approval_callback


from loader import dp, bot

from states import RegistrationProcess


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Please choose what you need", reply_markup=menu)



@dp.message_handler(text="🔑Register🔑", state=RegistrationProcess.RegisteredPerson)
async def double_registration(message: types.Message):
    await message.answer("🙄Hey, you are already registered in our database🙄")


@dp.message_handler(text="🔑Register🔑")
async def secret_question(message: types.Message):
    await message.answer("🔒Please type the <b>name of our landlord</b> to prove that you are resident🔒")
    await RegistrationProcess.NotApprovedResident.set()



@dp.message_handler(text="Thor", state=RegistrationProcess.NotApprovedResident)
async def approved_resident(message: types.Message, state: FSMContext):
    await message.answer("Now we can believe you 😉\n\n"
                         "Please type your ℹ️ <b>FIRST NAME</b> ℹ️ in <b>English format</b>\n\n")

    await RegistrationProcess.FirstName.set()



@dp.message_handler(state=RegistrationProcess.FirstName)
async def residents_first_name(message: types.Message, state: FSMContext):
    first_name = message.text
    await state.update_data(first_name=first_name)
    await message.answer("Now please type your ℹ️ <b>LAST NAME</b> ℹ️ in <b>English format</b>\n\n")

    await RegistrationProcess.LastName.set()


@dp.message_handler(state=RegistrationProcess.LastName)
async def residents_last_name(message: types.Message, state: FSMContext):
    last_name = message.text
    await state.update_data(last_name=last_name)
    await message.answer("Now please type your 📧 <b>E-MAIL</b> 📧\n\n")

    await RegistrationProcess.Email.set()


@dp.message_handler(state=RegistrationProcess.Email)
async def residents_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer(text="Have you arrived in 🇩🇰 <b>Copenhagen</b> 🇩🇰?", reply_markup=arrival_choice)

    await RegistrationProcess.ArrivalStatus.set()


@dp.callback_query_handler(arrival_callback.filter(check="yes"), state=RegistrationProcess.ArrivalStatus)
async def arrival_status(call: CallbackQuery, state: FSMContext, callback_data: dict):
    arrival = callback_data.get("arrival_status")
    await state.update_data(arrival=arrival)
    await call.message.answer("🗝Please choose the room you have been allocated to🗝", reply_markup=room_choice)

    await RegistrationProcess.RoomNumber.set()


@dp.callback_query_handler(choose_callback.filter(room="yes"), state=RegistrationProcess.RoomNumber)
async def choosing_room(call: CallbackQuery, state: FSMContext, callback_data: dict):
    room = callback_data.get("room_number")
    await state.update_data(room=room)
    data = await state.get_data()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    arrival = data.get("arrival")
    await call.message.answer(f"You've chosen <b>room {room}</b>\n\n")
    await call.message.answer(f"Is the information correct?\n"
                              f"Your name: <b>{first_name}</b>\n"
                              f"Your last name: <b>{last_name}</b>\n"
                              f"Your email: <b>{email}</b>\n"
                              f"Your arrival status: <b>{arrival}</b>\n"
                              f"Your room number in KK: <b>{room}</b>",
                              reply_markup=approval_choice)

    # await state.reset_state()


@dp.callback_query_handler(text="Exit", state=RegistrationProcess.RoomNumber)
async def cancel_choosing(call: CallbackQuery, state: FSMContext):
    await call.answer("😥You haven't chosen your room😥\n\n"
                      "Please start registration again!", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
    await state.reset_state()


@dp.callback_query_handler(approval_callback.filter(approval_status="Correct"), state=RegistrationProcess.RoomNumber)
async def approved_status(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.message.answer("⭐️You are successfully registered in TheMark database, we will contact with you soon⭐️")
    await RegistrationProcess.RegisteredPerson.set()


@dp.callback_query_handler(approval_callback.filter(approval_status="Incorrect"), state=RegistrationProcess.RoomNumber)
async def approved_status(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.message.answer("⚠️ Please register yourself again ⚠️️")
    await state.reset_state()



@dp.message_handler(text="📱Contacts📱")
async def get_contacts(message: types.Message):
    await message.answer("+45 26 61 34 13 - <b>Thor</b> (<i>KK's landlord</i>)\n\n"
                         "<a href='https://themark.dk'>TheMark</a> (Click on it if you wanna visit our website)")