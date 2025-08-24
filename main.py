import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command

from os import getenv
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def commands_start_handler(message: Message):
    await message.reply('!')









async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


