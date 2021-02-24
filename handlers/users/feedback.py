from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.default import menu
from keyboards.inline.readiness_choice_buttons import readiness_choice
from keyboards.inline.readiness_callback_datas import readiness_callback
from states import RegistrationProcess, Feedback


from loader import dp, bot
from aiogram import types



@dp.message_handler(text="😊Feedback😊", state=Feedback.GaveFeedback)
async def gave_feedback(message: types.Message, state: FSMContext):
    await message.answer("🙊 This section is not available to you, you already gave your feedback 🙊")


@dp.message_handler(text="😊Feedback😊", state=RegistrationProcess.RegisteredPerson)
async def ready_or_not(message: types.Message, state: FSMContext):
    await message.answer("⚠️<b>WARNING</b>⚠️\n\n"
                         "1️⃣ You have only <b>1 attempt</b> to write your FEEDBACK 1️⃣\n\n"
                         "😉 Please click on <b>\"READY\"</b> button if you are ready to give your <i>FINAL FEEDBACK ABOUT KK</i> 😉\n\n"
                         "😯 If you feel that you not ready yet, choose <b>\"NOT READY\"</b> 😯\n\n"
                         "🔥 Remember: <b>ONLY 1 ATTEMPT</b> 🔥\n\n"
                         "😲 Are you completely ready to write your final FEEDBACK? 😲",
                         reply_markup=readiness_choice)


@dp.message_handler(text="😊Feedback😊")
async def not_registered_feedback(message: types.Message):
    await message.answer(text="🔑Please register to proceed🔑\n\n", reply_markup=menu)


@dp.callback_query_handler(readiness_callback.filter(readiness_status="Ready"), state=RegistrationProcess.RegisteredPerson)
async def ready_choice(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.message.answer("🤠 It seems like you are ready to give your feedback! 🤠\n\n"
                              "Please feel free to type your feedback in a chat 😉")

    await Feedback.GivingFeedback.set()

@dp.message_handler(state=Feedback.GivingFeedback)
async def answer_feedback(message: types.Message, state: FSMContext):
    feedback = message.text
    await state.update_data(feedback=feedback)
    await message.answer(text="🥰 Thank you for your feedback 🥰", reply_markup=menu)
    sticker_file_id = "CAACAgIAAxkBAAIJHmAxKHZmEo2EsIewjsn5PShc_3DKAAIiAwACbbBCA7zHw9-hcLV4HgQ"
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=sticker_file_id)
    await Feedback.GaveFeedback.set()

@dp.callback_query_handler(readiness_callback.filter(readiness_status="Not Ready"), state=RegistrationProcess.RegisteredPerson)
async def not_ready_choice(call: CallbackQuery, state: FSMContext):
    await call.message.answer("🥺 It's ok, take your time and come back to this section when you feel ready 🥺")