from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, Message, CallbackQuery

from keyboards.inline.video_choice_buttons import video_choice
from keyboards.inline.video_callback_datas import video_callback

from loader import dp, bot



@dp.message_handler(content_types=ContentType.VIDEO)
async def git_file_id(message:Message):
    await message.reply(message.video.file_id)



@dp.message_handler(Command("videos"))
async def choosing_videos(message: types.Message):
    await message.answer(text="Please choose the video you want to get access to!", reply_markup=video_choice)



@dp.callback_query_handler(video_callback.filter(video_type="Laundry"))
async def choosing_laundry(call: CallbackQuery):
    await call.answer(cache_time=60)
    video_file_id = "BAACAgIAAxkBAAIB92AqPfToMFBhcmuCFPeAy6KmmJZUAALQCgACkIVRSaAdxqP11QLHHgQ"
    await bot.send_video(chat_id=call.from_user.id,
                         video=video_file_id,
                         caption="ℹ️Information about <b>Laundry Room</b>ℹ️")



@dp.callback_query_handler(video_callback.filter(video_type="Trash"))
async def choosing_laundry(call: CallbackQuery):
    await call.answer(cache_time=60)
    video_file_id = "BAACAgIAAxkBAAICDWAqQKL-vrDasyob2jxz-q0VH-sTAALdCgACkIVRSZHyYlCb5aHLHgQ"
    await bot.send_video(chat_id=call.from_user.id,
                         video=video_file_id,
                         caption="ℹ️Information about <b>Trash Sorting</b>ℹ️")



@dp.callback_query_handler(video_callback.filter(video_type="Linen"))
async def choosing_laundry(call: CallbackQuery):
    await call.answer(cache_time=60)
    video_file_id = "BAACAgIAAxkBAAICD2AqQKr-BH0voAHO6EWL0sd1oPvCAALeCgACkIVRScmjGb42ypg5HgQ"
    await bot.send_video(chat_id=call.from_user.id,
                         video=video_file_id,
                         caption="ℹ️Information about <b>Changing Bed Linen</b>ℹ️")



@dp.callback_query_handler(video_callback.filter(video_type="Access"))
async def choosing_laundry(call: CallbackQuery):
    await call.answer(cache_time=60)
    video_file_id = "BAACAgIAAxkBAAICC2AqQJd4UoYsumUC6zSJqrczt6o2AALcCgACkIVRSd35OWPVF7EVHgQ"
    await bot.send_video(chat_id=call.from_user.id,
                         video=video_file_id,
                         caption="ℹ️Information about <b>Proper Access to KK</b>ℹ️")



@dp.callback_query_handler(text="Exit")
async def choosing_cancel(call: CallbackQuery):
    await call.answer("😥You've canceled the operation😥", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)

