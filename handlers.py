from load import dp

from aiogram import types

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db import create_connection, create_table, add_to_table, watch_table

from config import TOKEN_API

from inline_keyboard import get_keyboard, sat_inline_keyboard, ielts_inline_keyboard, add_inline_keyboard
from reply_keyboard import sat_reply_keyboard

from reply_keyboard import add_reply_keyboard

@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await message.answer('Данный бот умеет отправлять рандомные символы латинского алфавита')

@dp.message_handler(commands=['get'])
async def get_command(message: types.Message):
    await message.answer('Данный бот умеет отправлять рандомные символы латинского алфавита', reply_markup=get_keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def get_cb_handler(callback: types.CallbackQuery) -> None:
    if callback.data == "btn_sat":
        await callback.message.answer('Следующий шаг', reply_markup=sat_inline_keyboard)
        await callback.message.delete()
    elif callback.data == "btn_ielts":
        await callback.message.answer('Следующий шаг', reply_markup=ielts_inline_keyboard)
        await callback.message.delete()

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('sat'))
async def sat_cb_handler(callback: types.CallbackQuery) -> None:
    if callback.data == "sat_verbal":
        await callback.message.answer('Следующий шаг', reply_markup=sat_reply_keyboard)
    elif callback.data == "sat_math":
        pass


# ADMIN
@dp.message_handler(commands=['admin'])
async def desc_command(message: types.Message):
    await message.answer('Можете добавить книгу, нажав на кнопку ниже', reply_markup = add_inline_keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('button'))
async def add_cb_handler(callback: types.CallbackQuery) -> None:
    if callback.data == "button_watch":
        result = watch_table("all")
        msg = ""
        
        try:
            for element in result:
                i = 0
                while i < len(element):
                    msg += str(element[i])
                    i += 1
                    msg += " "
                msg += "\n"
                
            await callback.message.answer(msg)
        except:
            print(f"The error occurred")

    elif callback.data == "button_add":   
        #add_to_table("idi nahui", "sat_math")

        await callback.message.answer('Начинаем добавлять!', reply_markup=add_reply_keyboard)

    
    await callback.message.delete()