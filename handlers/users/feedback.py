from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery


from loader import dp
from aiogram import types

from states import Survey

@dp.message_handler(Command('feedback'))
async def enter_feedback(message: types.Message):
    await message.answer("Now you are about to give a feedback!\n\n"
                         "⬇️Question 1⬇️\n\n"
                         "Have you ever had problems with sink?")

    await Survey.Q1.set()


@dp.message_handler(state=Survey.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("⬇️Question 2⬇️\n\n"
                         "Have you ever noticed that people organized parties and didn't invite you?")

    await Survey.Q2.set()




@dp.message_handler(state=Survey.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("🧡Thank you for your feedback!🧡")
    await message.answer(f"Answer1: {answer1}")
    await message.answer(f"Answer2: {answer2}")

    await state.reset_state()

