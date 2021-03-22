from aiogram.dispatcher import FSMContext
from aiogram import types
from states import RegistrationProcess, Feedback, Complain
from aiogram.types import CallbackQuery
from loader import dp, bot
from keyboards.inline.complaint_choice_buttons import complaint_choice
from keyboards.inline.complaint_callback_datas import complaint_callback
from data.config import GAVE_FEEDBACK


@dp.message_handler(text="👮‍Complain👮‍", state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def complain_function(message: types.Message):
    sticker_file_id = "CAACAgIAAxkBAAISfGA6nATMMqMTtVRY3IaXbvRkp4dlAAIJAwACbbBCA6-5xc2si2vxHgQ"
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=sticker_file_id)
    await message.answer(text="If you really need to complain, please click <b>\"Complain\"</b> button below\n"
                              "Otherwise click <b>\"Cancel operation\"</b>", reply_markup=complaint_choice)


@dp.callback_query_handler(complaint_callback.filter(complain_status="yes"), state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def new_status(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.message.answer(text="Now please describe your problem in the chat and <b>try to reveal it in as much detail as possible</b>\n\n"
                           "<i>Our landlord will contact you within <b>24 hours</b> to handle your problem</i>\n\n"
                           "🔥 If there is a serious problem and you have to resolve it immediately, write to our landlord on WhatsApp or call him 🔥\n\n"
                           "<b>Thor's phone number: +45 26 61 34 13</b>")
    await Complain.TypingComplain.set()


@dp.message_handler(state=Complain.TypingComplain)
async def new_complain(message: types.Message, state: FSMContext):
    complain = message.text
    id = message.from_user.id
    await state.update_data(complain=complain)
    data = await state.get_data()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    room_number = data.get("room")
    await bot.send_message(chat_id=1643618473, text=f"<b>🤬 COMPLAINT 🤬</b>\n\nResident <b>{first_name} {last_name}</b> who is living in <b>room {room_number}</b> has complained:\n\n<b>Complaint:</b> {complain}")
    await message.answer("⌛ Your complain has been sent to the landlord successfully, wait for response ⌛")
    if id in GAVE_FEEDBACK:
        await Feedback.GaveFeedback.set()
    else:
        await RegistrationProcess.RegisteredPerson.set()


@dp.callback_query_handler(text="cancel", state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def new_status(call: CallbackQuery):
    await call.answer(text="😓 You've canceled the operation 😓", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)



