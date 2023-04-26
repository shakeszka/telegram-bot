from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from config import TOKEN_API

from reply_keyboard import add_reply_keyboard, cancel_reply_keyboard

from load import dp

from aiogram import types

from aiogram.dispatcher.filters import Text

from db import add_to_table

storage = MemoryStorage()


class AdminStatesGroup(StatesGroup):
    doc = State()
    category = State()


# CANCEL ХУЙНЯ
@dp.message_handler(commands=['cancel'], state='*')
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.reply('Отменил', reply_markup=add_reply_keyboard)
    await state.finish()


@dp.message_handler(Text(equals='Начать работу!', ignore_case=True), state=None)
async def start_work(message: types.Message, state: FSMContext):
    await AdminStatesGroup.doc.set()
    await message.answer('Сначала отправь документ! Можете отправить ссылку или файл.', reply_markup=cancel_reply_keyboard)

@dp.message_handler(state=AdminStatesGroup.doc)
async def load_doc(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['doc'] = message.text

    await AdminStatesGroup.next()
    await message.answer("Какая категория?")


@dp.message_handler(state=AdminStatesGroup.category)
async def load_category(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['category'] = message.text

    add_to_table(data['doc'], data['category'])
    await message.reply('Ваш документ сохранен!')

    await state.finish()