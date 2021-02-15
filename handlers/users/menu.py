from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.default import menu
from keyboards.inline.room_choice_buttons import room_choice
from keyboards.inline.room_callback_datas import choose_callback
from loader import dp, bot

from states import RegistrationProcess

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Please choose what you need", reply_markup=menu)



@dp.message_handler(text="🔑Register🔑")
async def registration(message: types.Message):
    await message.answer("Please type your full name below: ")

    await RegistrationProcess.FullName.set()



@dp.message_handler(state=RegistrationProcess.FullName)
async def answer_FullName(message: types.Message, state: FSMContext):
    await message.answer("✅You are successfully registered in our database✅")
    await state.reset_state()



@dp.message_handler(text="📱Contacts📱")
async def get_contacts(message: types.Message):
    await message.answer("+45 26 61 34 13 - <b>Thor</b> (<i>KK's landlord</i>)\n\n"
                         "<a href='https://themark.dk'>TheMark</a> (Click on it it you wanna visit our website)")



@dp.message_handler(text="🏠Arrival status🏠")
async def arrival_status(message:types.Message):
    await message.answer(text="🗝Please choose the room you have been allocated to🗝",
                         reply_markup=room_choice)



@dp.callback_query_handler(choose_callback.filter(room="yes"))
async def choosing_room(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    room = callback_data.get("room_number")
    await call.message.answer(f"You've chosen room {room}. Thanks!")


@dp.callback_query_handler(text="Exit")
async def cancel_choosing(call: CallbackQuery):
    await call.answer("😥You've canceled the operation😥", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)