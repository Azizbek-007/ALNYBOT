from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import schedule
import asyncio


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


CHAT_ID = 123456789  # Replace with your chat ID
GROUP_ID = -1001823734059  # Replace with your group ID


async def send_message():
    await dp.bot.send_message(GROUP_ID, "Hello, this message was sent every 5 seconds!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
   
