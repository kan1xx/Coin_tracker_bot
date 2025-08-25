import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from os import getenv
from dotenv import load_dotenv
from texts import START_TEXT
from api import get_info

load_dotenv()
BOT_TOKEN = getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

Coins_choose_keyboard = ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text='BTC')],
    [KeyboardButton(text='ETH')],
    [KeyboardButton(text='TON')]    
    ],resize_keyboard=True)
    

@dp.message(Command('start'))
async def commands_start_handler(message: Message):
    await message.reply(START_TEXT, parse_mode='HTML')

@dp.message()
async def get_info_about_coin(message: Message):
    try:
        symbol = message.text.upper() + 'USDT'
        data = await get_info(symbol)

        formatted_price = format(float(data['lastPrice']), '.2f')
        formatted_high_price = format(float(data['highPrice']), '.2f')
        formatted_low_price = format(float(data['lowPrice']), '.2f')
        formatted_price_change_percent = format(float(data['priceChangePercent']), '.2f')
        formatted_volume = format(float(data['volume']), '.2f')

        await message.reply(
        f'Info about: <b>{symbol}</b>\n'
        f'💰 <b>Currently price:</b> ${formatted_price}\n'
        f'🔺 <b>Highest price for 24 hours:</b> {formatted_high_price}\n'
        f'🔻 <b>Lowest price for 24 hours:</b> {formatted_low_price}\n'
        f'📈 <b>Price change percent: </b> {formatted_price_change_percent}\n'
        f'📊 <b>Volume:</b> {formatted_volume}\n',
        parse_mode='HTML'
       )
    except KeyError:
        await message.reply('Incorrect quote!')


    


    

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


