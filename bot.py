import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Это бот для скупки предметов из Roblox.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
