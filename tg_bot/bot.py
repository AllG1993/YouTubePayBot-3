import os
import sys


sys.path.insert(0, os.path.abspath(''))
sys.path.insert(1, os.path.abspath('..'))
sys.path.insert(1, r'C:\\Users\\Aleksey\\PycharmProjects\\TGBots\\YouTubePayBot-3')
print(sys.path)
from aiogram import executor

from tg_bot.handlers.commands import im, start_help, paid
from filters.is_trusted_user import IsTrustedUser
from tg_bot.loader import dp


dp.filters_factory.bind(IsTrustedUser)

dp.register_message_handler(start_help, commands=['start', 'help'], is_trusted_user=True)
dp.register_message_handler(im, commands='im', is_trusted_user=True)
dp.register_message_handler(paid, commands='paid', is_trusted_user=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
