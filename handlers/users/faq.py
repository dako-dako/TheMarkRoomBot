from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states import RegistrationProcess, Feedback


from keyboards.default import menu



@dp.message_handler(text="ℹ️FAQℹ️", state=[RegistrationProcess.RegisteredPerson, Feedback.GaveFeedback])
async def bot_info(message: types.Message, state:FSMContext):
    text = ("This section is dedicated to <b>Frequently Asked Questions (FAQ)</b>",
            "Below you can find these questions and answers to them as well!\n",
            "<i>How can I connect to WiFi?</i>",
            "<b>Answer:</b> In your WiFi list find \"Katherine Kollegiet\", the password is \"TheMark2000\", that's pretty much it!\n",
            "<i>Is there laundry room in KK?</i>",
            "<b>Answer:</b> Of course we have it! It is located in a basement.\nTo know more click \"🎞Videos🎞\" button\n",
            "<i>Who is responsible for the dorm - <b>Katherine Kollegiet</b>?</i>",
            "<b>Answer:</b> <b>Thor</b> - he is our <b>landlord</b>, if you have any problems with your room or just want to talk to somebody nice, talk to him!\n"
            "His telephone - <b>+45 26 61 34 13</b>.\nTo know more click \"📱Contacts📱\" button")
    await message.answer(text="\n".join(text), reply_markup=menu)


@dp.message_handler(text="ℹ️FAQℹ️")
async def not_registered_faq(message: types.Message):
    await message.answer(text="🔑Please register to proceed🔑", reply_markup=menu)