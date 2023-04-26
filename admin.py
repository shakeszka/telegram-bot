@dp.message_handler(commands=['add'])
async def desc_command(message: types.Message):
    await message.answer('Можете добавить книгу')