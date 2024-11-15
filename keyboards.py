from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


sched_button = InlineKeyboardButton(text='▶️', callback_data='Zapusk' )

first_inline_kb = InlineKeyboardMarkup(
            inline_keyboard=[[sched_button]])


