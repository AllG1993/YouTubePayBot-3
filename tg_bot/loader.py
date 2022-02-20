import logging

from aiogram import Bot, Dispatcher

API_TOKEN = '5185504704:AAFsopDxY9PqAHmrqex9Dp1aMpNb6WeKvmM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize tg_bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
