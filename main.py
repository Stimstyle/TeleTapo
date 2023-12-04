import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
    

@dp.message_handler(commands=['get_video'])
async def get_video(message: types.Message):
    # Код для взаимодействия с TP Link/Tapo API
    # Получение изображения или видео с камеры
    video = ... # Здесь должен быть ваш код для получения видео

    # Отправка видео пользователю
    await message.reply_video(video)



if __name__ == '__main__':
    asyncio.run(main())
