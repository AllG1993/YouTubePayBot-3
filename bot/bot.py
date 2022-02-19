import logging
from aiogram import Bot, Dispatcher, executor, types

from filters.is_trusted_user import IsTrustedUser

import tst

API_TOKEN = '2103581748:AAFmfEII4cEkdXxUJPqp4uWldtv91qDAwGk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.filters_factory.bind(IsTrustedUser)

dp.register_message_handler(tst.hi, commands='hi', is_trusted_user=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
