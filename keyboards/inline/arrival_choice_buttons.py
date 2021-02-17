from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.arrival_callback_datas import arrival_callback

arrival_choice = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="❇️ I have Arrived ❇️", callback_data=arrival_callback.new(arrival_status="Arrived", check="yes")),
                                          ],
                                          [
                                              InlineKeyboardButton(text="❌ I haven't arrived yet ❌", callback_data=arrival_callback.new(arrival_status="Not Arrived", check="yes")),
                                          ],
                                      ])