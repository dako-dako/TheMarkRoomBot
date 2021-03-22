from aiogram import types
from loader import dp

from aiogram.dispatcher.filters import Command
from states import RegistrationProcess, Feedback

from data.config import ADMINS, RESIDENTS_ARRIVED, RESIDENTS_NOT_ARRIVED


@dp.message_handler(Command('residents'), user_id=[1643618473, 736483526], state=[RegistrationProcess.RegisteredPerson, None, Feedback.GaveFeedback])
async def admin_arrival_check(message: types.Message):
    await message.answer("Below you can find list of <b>ARRIVED RESIDENTS</b>")
    for k, res_list in RESIDENTS_ARRIVED.items():
        await message.answer("Resident: <b>" + res_list[0] + " " + res_list[1] + " room " + res_list[3] + "</b> (" + res_list[2] + ")\n")


    await message.answer("Below you can find list of <b>RESIDENTS WHO HAVEN'T ARRIVED YET</b>")
    for k, not_res_list in RESIDENTS_NOT_ARRIVED.items():
        await message.answer("Resident <b>" + not_res_list[0] + " " + not_res_list[1] + " room " + not_res_list[3] + "</b> (" + not_res_list[2] + ")\n")