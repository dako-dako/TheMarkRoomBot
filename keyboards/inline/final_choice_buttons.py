from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.final_callback_datas import final_callback

final_choice = InlineKeyboardMarkup(row_width=1,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text="🇩🇰 I have arrived in Copenhagen 🇩🇰", callback_data=final_callback.new(arrival_status="Arrived")),
                                        ],
                                        [
                                            InlineKeyboardButton(text="Cancel operation", callback_data="cancel")
                                        ],
                                    ])