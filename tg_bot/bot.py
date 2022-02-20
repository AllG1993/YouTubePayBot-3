import os
import sys

from aiogram import executor

from tg_bot.handlers.commands import im, start_help, paid
from filters.is_trusted_user import IsTrustedUser
from tg_bot.loader import dp

sys.path.insert(0, os.path.abspath('..'))
dp.filters_factory.bind(IsTrustedUser)

dp.register_message_handler(start_help, commands=['start', 'help'], is_trusted_user=True)
dp.register_message_handler(im, commands='im', is_trusted_user=True)
dp.register_message_handler(paid, commands='paid', is_trusted_user=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
