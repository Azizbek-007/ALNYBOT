from aiogram import types
from loader import dp
from utils.db_api import DBS
import math
import time
from keyboards.inline import added_btn
import asyncio

@dp.message_handler(content_types=types.ContentType.ANY, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def any(msg: types.Message):
    user_data = await dp.bot.get_chat_member(msg.chat.id, msg.from_id)
    if user_data.status == 'admin' or user_data.status == "restricted":
        count_data = DBS.reckon_count(DBS, msg.from_id, msg.chat.id)
        data = DBS.GetQuantity(DBS)
        add_count = data - count_data
        if count_data < data:
            await msg.delete()
            get = await msg.answer(f"<a href='tg://user?id={msg.from_id}'>{msg.from_user.full_name}</a> Для размещения объявления необходимо добавить в группу не менее {add_count} человек.", 'HTML', reply_markup=added_btn(msg.from_id))
            await dp.bot.restrict_chat_member(
                            chat_id=msg.chat.id,
                            user_id=msg.from_id,
                            until_date=math.floor(time.time()) + 1*60,
                            permissions=types.ChatPermissions(
                                        can_send_messages=False, 
                                        can_invite_users=True
                                    )
                            )
            await asyncio.sleep(60)
            await dp.bot.delete_message(msg.chat.id, get.message_id)
        
@dp.callback_query_handler(lambda call: call.data.startswith("added="))
async def mem_added(call: types.CallbackQuery):
    call_user_id = call.data.split('=')[1]
    if str(call_user_id) == str(call.from_user.id):
        user_count = DBS.GetUserCount(DBS, call.from_user.id, chat_id=call.message.chat.id)
        data = DBS.GetQuantity(DBS)
        add_count = data - user_count
        if user_count < data:
            await call.answer(f"Для размещения объявления необходимо добавить в группу не менее {add_count} человек.", True)
        else:
            await call.message.delete()
            await dp.bot.restrict_chat_member(
                call.message.chat.id,
                call.from_user.id,
                can_send_messages=True
            )
    else: await call.answer("Это команда не для вас", True)