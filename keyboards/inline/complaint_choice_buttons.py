from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.complaint_callback_datas import complaint_callback


complaint_choice = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text="😡 Complain 😡", callback_data=complaint_callback.new(complain_status="yes"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="Cancel operation", callback_data="cancel")
                                            ]
                                        ])




