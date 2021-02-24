from aiogram.dispatcher import FSMContext
from aiogram import types
from states import RegistrationProcess, Feedback
from aiogram.types import CallbackQuery
from keyboards.default import menu
from loader import dp
from keyboards.inline.final_choice_buttons import final_choice
from keyboards.inline.final_callback_datas import final_callback
from utils.dp_api import quick_commands as commands

@dp.message_handler(text="🛫Arrival Status🛫", state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def yes_or_not(message: types.Message, state: FSMContext):
    data = await state.get_data()
    current_status = data.get("arrival")
    if current_status == "Not Arrived":
        await message.answer(text=f"⚠️ <b>Please read this carefully</b> ⚠️\n\n"
                                  f"Right now your arrival status is: <b>\"{current_status}\"</b>\n\n"
                                  f"If you are not in Copenhagen yet, click <i>\"Cancel operation\"</i> and come back to this section when you are in Copenhagen\n\n"
                                  f"If you need to change your status from <i>\"Not arrived\"</i> to <i>\"Arrived\"</i>, please click the button below\n"
                                  f"🔥 <b>But remember, you have only 1 attempt to change arrival status!</b> 🔥",
                             reply_markup=final_choice)
    else:
        await message.answer(text=f"Your current arrival status is: <b>{current_status}</b>\n\n"
                                  f"This section is not meant for you 😉")


@dp.callback_query_handler(final_callback.filter(arrival_status="Arrived"), state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def new_status(call: CallbackQuery, state: FSMContext, callback_data: dict):
    arrival = callback_data.get("arrival_status")
    await state.update_data(arrival=arrival)
    data = await state.get_data()
    arrival = data.get("arrival")
    user_id = call.from_user.id
    await commands.update_resident_arrival_status(id=user_id, resident_arrival_status=arrival)
    await call.message.answer(text="Your status was successfully changed 😉", reply_markup=menu)


@dp.callback_query_handler(text="cancel", state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def new_status(call: CallbackQuery):
    await call.answer(text="😓 You've canceled the operation 😓", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)