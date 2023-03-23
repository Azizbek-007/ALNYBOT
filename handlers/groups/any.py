from aiogram import types
from loader import dp
from utils.db_api import DBS
import math
import time
@dp.message_handler(content_types=types.ContentType.ANY, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def any(msg: types.Message):
    count_data = DBS.reckon_count(DBS, msg.from_id, msg.chat.id)
    if count_data == 0:
        await msg.delete()
        await dp.bot.restrict_chat_member(
                        chat_id=msg.chat.id,
                        user_id=msg.from_id,
                        until_date=math.floor(time.time()) + 3*60,
                        permissions=types.ChatPermissions(
                                    can_send_messages=False, 
                                    can_invite_users=True
                                )
                        )