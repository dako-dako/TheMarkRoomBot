from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.readiness_callback_datas import readiness_callback

readiness_choice = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text="😎 READY 😎", callback_data=readiness_callback.new(readiness_status="Ready"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="⚠️ NOT READY ⚠️", callback_data=readiness_callback.new(readiness_status="Not Ready"))
                                            ],
                                        ])