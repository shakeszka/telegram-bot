from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sat_reply_keyboard = ReplyKeyboardMarkup(keyboard=[["Book 1"], ["Book 2"]])
add_reply_keyboard = ReplyKeyboardMarkup(keyboard=[["Начать работу!"]])
cancel_reply_keyboard = ReplyKeyboardMarkup(keyboard=[["/cancel"]])