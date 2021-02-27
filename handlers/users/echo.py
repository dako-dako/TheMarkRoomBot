from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import register_menu
from loader import dp
from states import RegistrationProcess, Feedback


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(text="🔑Please register to proceed🔑\n\n", reply_markup=register_menu)


@dp.message_handler(state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def bot_echo(message: types.Message):
    await message.answer(f"No such command:\n\n"
                         f"{message.text}")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"{message} {state}")
