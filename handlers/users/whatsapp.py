from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states import RegistrationProcess, Feedback
from keyboards.default import menu
from keyboards.inline.whatsapp_url_button import whatsapp_button



@dp.message_handler(text="✌️WhatsApp Group✌️", state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def not_registered_whatsapp(message: types.Message, state: FSMContext):
    await message.answer("💻 Join KK WhatsApp group! 💻", reply_markup=whatsapp_button)


@dp.message_handler(text="✌️WhatsApp Group✌️")
async def not_registered_whatsapp(message: types.Message):
    await message.answer(text="🔑Please register to proceed🔑", reply_markup=menu)