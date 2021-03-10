from aiogram import types
from loader import dp

from aiogram.dispatcher.filters import Command
from states import RegistrationProcess, Feedback

from data.config import ADMINS

@dp.message_handler(Command('thor'), user_id=ADMINS, state=[RegistrationProcess.RegisteredPerson, None, Feedback.GaveFeedback])
async def admin_chat_command(message: types.Message):
    await message.answer("This is a secret message especially for Thor\n\n"
                         "To prove him that it's working")