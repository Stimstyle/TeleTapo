import asyncio
import logging
import os

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(text=message.text)
    
    
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
    





if __name__ == '__main__':
    asyncio.run(main())
