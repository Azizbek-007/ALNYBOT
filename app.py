from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.admin import SendMessageToAll
import schedule
import asyncio


# async def on_startup(dispatcher):
#     # Birlamchi komandalar (/star va /help)
#     await set_default_commands(dispatcher)

#     # Bot ishga tushgani haqida adminga xabar berish
#     await on_startup_notify(dispatcher)


CHAT_ID = 123456789  # Replace with your chat ID
GROUP_ID = -1001823734059  # Replace with your group ID


async def send_message():
    await dp.bot.send_message(GROUP_ID, "Hello, this message was sent every 5 seconds!")


async def scheduled(wait_for):
    schedule.every(wait_for).seconds.do(send_message)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(5))
    executor.start_polling(dp, skip_updates=True, loop=loop)
   
