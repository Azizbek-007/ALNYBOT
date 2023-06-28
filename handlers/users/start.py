from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp

from utils.db_api.func import DBS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    DBS.user_register(message.from_id, message.from_user.username, message.from_user.first_name)
    await message.answer(f"Hi, {message.from_user.full_name}!")
