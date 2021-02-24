from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states import RegistrationProcess, Feedback


from keyboards.default import menu


@dp.message_handler(text="📱Contacts📱", state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def get_contacts_registered(message: types.Message, state: FSMContext):
    await message.answer("+45 26 61 34 13 - <b>Thor</b> (<i>KK's landlord</i>)\n\n"
                         "<a href='https://themark.dk'>TheMark</a> (Click on it if you wanna visit our website)")

@dp.message_handler(text="📱Contacts📱")
async def get_contacts_unregistered(message: types.Message):
    await message.answer(text="🔑Please register to proceed🔑", reply_markup=menu)