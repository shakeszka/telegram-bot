from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

get_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('SAT', callback_data='btn_sat')],
    [InlineKeyboardButton('IELTS', callback_data='btn_ielts')]
])

add_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('WATCH ALL', callback_data='button_watch')],
    [InlineKeyboardButton('ADD', callback_data='button_add')]
])

sat_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Verbal', callback_data='sat_verbal')],
    [InlineKeyboardButton('Math', callback_data='sat_math')]
])

ielts_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Listening', callback_data='ielts_listening')],
    [InlineKeyboardButton('Reading', callback_data='ielts_reading')]
])

