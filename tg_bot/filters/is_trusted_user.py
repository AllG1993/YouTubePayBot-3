import os
from pathlib import Path

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from users.users import User
from google_sheets_api.sheets import SpreadsheetProcessor


creds_path = Path(Path.cwd().parent, '/ytpb-3-test-creds.json')

spreadsheet_handler = SpreadsheetProcessor('11Uon-RJ_NahW-hAJiCb78zhstKOUDRw6nh_4hL9XI4A')


class IsTrustedUser(BoundFilter):
    key = 'is_trusted_user'

    def __init__(self, is_trusted_user):
        self.is_trusted_user = is_trusted_user

    async def check(self, message: types.Message):
        return User(message.from_user.id, spreadsheet_handler).trusted_user




