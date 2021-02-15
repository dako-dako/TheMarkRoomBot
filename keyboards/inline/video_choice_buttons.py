from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.video_callback_datas import video_callback

video_choice = InlineKeyboardMarkup(row_width=1,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text="🧼Laundry Room🧼", callback_data=video_callback.new(video_type="Laundry"))
                                        ],
                                        [
                                            InlineKeyboardButton(text="♻️Sorting Trash♻️", callback_data=video_callback.new(video_type="Trash"))
                                        ],
                                        [
                                            InlineKeyboardButton(text="🛏Bed Linen🛏", callback_data=video_callback.new(video_type="Linen"))
                                        ],
                                        [
                                            InlineKeyboardButton(text="🔐Dorm Access🔐", callback_data=video_callback.new(video_type="Access"))
                                        ],
                                        [
                                            InlineKeyboardButton(text="🔴Exit🔴", callback_data="Exit")
                                        ],
                                    ])