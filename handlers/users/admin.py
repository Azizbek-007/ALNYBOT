from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.inline import admin_btn
from states import SetTime
from utils.db_api import DBS
import schedule
from aiogram.dispatcher import FSMContext

def validate_clock(clock_str):
    try:
        hour, minute = clock_str.strip().split(':')
        if int(hour) not in range(0, 24):
            return False

        if int(minute) not in range(0, 60):
            return False

        return True

    except ValueError:
        return False

    

@dp.message_handler(commands='admin')
async def bot_admin(message: types.Message):
    await SendMessageToAll()
    await message.answer("Hi admin", reply_markup=admin_btn())

@dp.callback_query_handler(text="SendMessage")
async def bot_SendMessage(call: types.CallbackQuery):
    await call.message.delete()
    await SetTime.promis.set()
    await call.message.answer("magan jiberiliw waqtin kiritn'")


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=SetTime.promis)
async def bot_SetTime(message: types.Message):
    if validate_clock(message.text):
        DBS.SetSchuldeTime(DBS, message.text)
        await SetTime.next()
        await message.answer("Xabar jiberin'")
    else: 
        await message.answer("Waqit qa'te kiritildi iltimas durs kiritin'!\n21:00")


@dp.message_handler(content_types=types.ContentTypes.ANY, state=SetTime.senMSG)
async def SetSendMessageToAll(message: types.Message, state: FSMContext):
    await state.finish()
    DBS.SetSettingData(DBS, message.from_user.id, message.message_id, message.reply_markup)
    await message.answer("Successfuly 200")

async def SendMessageToAll():
    data = DBS.GetSettingData(DBS)[0]
    print(11111)
    await dp.bot.copy_message(data[1], data[3], data[4])


