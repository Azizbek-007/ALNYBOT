from aiogram import types
from loader import dp
from utils.db_api import DBS
import math
import time
from keyboards.inline import added_btn
@dp.message_handler(content_types=types.ContentType.ANY, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def any(msg: types.Message):
    count_data = DBS.reckon_count(DBS, msg.from_id, msg.chat.id)
    if count_data == 0:
        await msg.delete()
        await msg.answer(f"<a href='tg://user?id={msg.from_id}'>{msg.from_user.full_name}</a> Odam qoshmasangiz guruhga yoza olamaysiz eng kamida bitta odam qoshing!", 'HTML', reply_markup=added_btn())
        await dp.bot.restrict_chat_member(
                        chat_id=msg.chat.id,
                        user_id=msg.from_id,
                        until_date=math.floor(time.time()) + 3*60,
                        permissions=types.ChatPermissions(
                                    can_send_messages=False, 
                                    can_invite_users=True
                                )
                        )
    
@dp.callback_query_handler(text="added")
async def mem_added(call: types.CallbackQuery):
    user_count = DBS.GetUserCount(DBS, call.from_user.id, chat_id=call.message.chat.id)
    if user_count == False:
        await call.answer("En' kemida 1 adam qosin'")
    else:
        await call.message.delete()
        data_permissions = await dp.bot.get_chat(call.message.chat.id)
        await dp.bot.restrict_chat_member(
            call.message.chat.id,
            call.from_user.id,
            can_send_messages=True
        )