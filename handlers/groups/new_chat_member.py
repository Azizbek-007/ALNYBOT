import math
import time
from aiogram import types
from loader import dp
from utils.db_api import DBS


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def new_chat_member_bot(msg: types.Message):
    new_members = msg.new_chat_members
    print(new_members)
    for x in new_members:
        if x.id != msg.from_id:
            DBS.add_count(DBS, msg.from_id, msg.chat.id)
    await msg.delete()


@dp.message_handler(content_types=types.ContentTypes.LEFT_CHAT_MEMBER, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def leftMember(msg: types.Message):
    await msg.delete()