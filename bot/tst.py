from aiogram import types

import users.users


async def hi(message: types.Message):
    user = users.users.User(message.from_user.id)
    await message.answer(f'Привет, {user.name}!\n'
                         f'Твоя роль: {user.role}')



