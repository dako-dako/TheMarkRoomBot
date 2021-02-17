from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.approval_callback_datas import approval_callback


approval_choice = InlineKeyboardMarkup(row_width=1,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(text="✅ Correct ✅", callback_data=approval_callback.new(approval_status="Correct")),
                                           ],
                                           [
                                               InlineKeyboardButton(text="🚫 Incorrect 🚫", callback_data=approval_callback.new(approval_status="Incorrect")),
                                           ],
                                       ])