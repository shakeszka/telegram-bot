from aiogram import executor

from db import create_connection, create_table

if __name__ == '__main__':
    from states import dp
    from handlers import dp

    create_connection()
    create_table()
    executor.start_polling(dp)