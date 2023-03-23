import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(chat_id=5356014595, text="Bot ON")

    except Exception as err:
        logging.exception(err)
