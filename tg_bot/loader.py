import logging

from aiogram import Bot, Dispatcher

API_TOKEN = None

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize tg_bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
