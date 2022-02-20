import os
from pathlib import Path

from aiogram import types

from datetime import datetime

from tg_bot.loader import bot

from users.users import User
from google_sheets_api.sheets import SpreadsheetProcessor


# creds_path = Path(Path.cwd().parent, r'ytpb-3-test-creds.json')
creds_path = os.path.dirname(os.path.abspath('')) + 'ytpb-3-test-creds.json'
spreadsheet_handler = SpreadsheetProcessor(creds_path, '11Uon-RJ_NahW-hAJiCb78zhstKOUDRw6nh_4hL9XI4A')


async def start_help(message: types.Message):
    user = User(message.from_user.id, spreadsheet_handler)
    await message.answer(f'Привет, {user.name}!\n'
                         f'Я тут смотрящий за ютюбом.\n'
                         f'Я как эпилепсия у старух - занимаюсь тряской бабок.\n\n'
                         f'Вот доступные команды:\n'
                         f'/help - ее результат ты видишь сейчас;\n'
                         f'/im - информация о тебе в моем сердечьке (базе данных);\n'
                         f'...;\n'
                         )


async def im(message: types.Message):
    """
    Сообщение с информацией о пользователе и его роли.
    :param message:
    :return:
    """
    user = User(message.from_user.id, spreadsheet_handler)
    await message.answer(f'Привет, {user.name}!\n'
                         f'Твоя роль: {user.role}')


async def paid(message: types.Message):
    user = User(message.from_user.id, spreadsheet_handler)
    spreadsheet_handler.append_table([[datetime.now().strftime('%d.%m.%y %H:%M'), user.name, user.id]], 'payments')
    await bot.send_message(user.id, '111')

if __name__ == '__main__':
    project_dir = Path.cwd()

