from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from users.users import User


class IsTrustedUser(BoundFilter):
    key = 'is_trusted_user'

    def __init__(self, is_trusted_user):
        self.is_trusted_user = is_trusted_user

    async def check(self, message: types.Message):
        return User(message.from_user.id).trusted_user




