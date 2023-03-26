from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.inline import admin_btn
from states import SetTime, SetTime4, SetTime3, SetTime2
from utils.db_api import DBS
import schedule
from aiogram.dispatcher import FSMContext

# def validate_clock(clock_str):
#     try:
#         hour, minute = clock_str.strip().split(':')
#         if int(hour) not in range(0, 24):
#             return False

#         if int(minute) not in range(0, 60):
#             return False

#         return True

#     except ValueError:
#         return False

    

@dp.message_handler(commands='admin')
async def bot_admin(message: types.Message):
    await message.answer("Hi admin", reply_markup=admin_btn())

@dp.callback_query_handler(text="SendMessage")
async def bot_SendMessage(call: types.CallbackQuery):
    await call.message.delete()
    await SetTime.promis.set()
    await call.message.answer("magan jiberiliw waqtin kiritn'")


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=SetTime.promis)
async def bot_SetTime(message: types.Message):
    DBS.SetSchuldeTime(DBS, message.text, 1)
    await SetTime.next()
    await message.answer("Xabar jiberin'")

@dp.message_handler(content_types=types.ContentTypes.ANY, state=SetTime.senMSG)
async def SetSendMessageToAll(message: types.Message, state: FSMContext):
    await state.finish()
    DBS.SetSettingData(DBS, message.from_user.id, message.message_id, message.reply_markup, 1)
    await message.answer("Successfuly 200")




@dp.callback_query_handler(text="SendMessage2")
async def bot_SendMessage2(call: types.CallbackQuery):
    await call.message.delete()
    await SetTime2.promis.set()
    await call.message.answer("magan jiberiliw waqtin kiritn'")


@dp.callback_query_handler(text="SendMessage3")
async def bot_SendMessage3(call: types.CallbackQuery):
    await call.message.delete()
    await SetTime3.promis.set()
    await call.message.answer("magan jiberiliw waqtin kiritn'")


@dp.callback_query_handler(text="SendMessage4")
async def bot_SendMessage4(call: types.CallbackQuery):
    await call.message.delete()
    await SetTime4.promis.set()
    await call.message.answer("magan jiberiliw waqtin kiritn'")




@dp.message_handler(content_types=types.ContentTypes.TEXT, state=SetTime2.promis)
async def bot_SetTime2(message: types.Message):
    # if validate_clock(message.text):
    DBS.SetSchuldeTime(DBS, message.text, 2)
    await SetTime2.next()
    await message.answer("Xabar jiberin'")

@dp.message_handler(content_types=types.ContentTypes.ANY, state=SetTime2.senMSG)
async def SetSendMessageToAll2(message: types.Message, state: FSMContext):
    await state.finish()
    DBS.SetSettingData(DBS, message.from_user.id, message.message_id, message.reply_markup, 2)
    await message.answer("Successfuly 200")




@dp.message_handler(content_types=types.ContentTypes.TEXT, state=SetTime3.promis)
async def bot_SetTime3(message: types.Message):
    # if validate_clock(message.text):
    DBS.SetSchuldeTime(DBS, message.text, 3)
    await SetTime3.next()
    await message.answer("Xabar jiberin'")

@dp.message_handler(content_types=types.ContentTypes.ANY, state=SetTime3.senMSG)
async def SetSendMessageToAll3(message: types.Message, state: FSMContext):
    await state.finish()
    DBS.SetSettingData(DBS, message.from_user.id, message.message_id, message.reply_markup, 3)
    await message.answer("Successfuly 200")


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=SetTime4.promis)
async def bot_SetTime4(message: types.Message):
    # if validate_clock(message.text):
    DBS.SetSchuldeTime(DBS, message.text, 4)
    await SetTime4.next()
    await message.answer("Xabar jiberin'")

@dp.message_handler(content_types=types.ContentTypes.ANY, state=SetTime4.senMSG)
async def SetSendMessageToAll4(message: types.Message, state: FSMContext):
    await state.finish()
    DBS.SetSettingData(DBS, message.from_user.id, message.message_id, message.reply_markup, 4)
    await message.answer("Successfuly 200")