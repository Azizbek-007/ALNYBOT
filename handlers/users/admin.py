from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default import admin_btn, back_btn, interview_btn
from keyboards.inline import delete_btn
from states import SateSetQuantity, SateSetLink, SateSetInterview, SateSetRandomPost, SateSetOprogram
from utils.db_api import DBS
import schedule
from aiogram.dispatcher import FSMContext

    

@dp.message_handler(text=["/admin", "⬅️Назад"], state="*")
async def bot_admin(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("👇 Выбирайте меню", reply_markup=admin_btn())


@dp.message_handler(text="Количество")
async def Quantity(msg: types.Message):
    await SateSetQuantity.promis.set()
    await msg.answer("Отправьте количество", reply_markup=back_btn)

@dp.message_handler(content_types=types.ContentTypes.ANY, state=SateSetQuantity.promis)
async def BotQuantity(msg: types.Message, state: FSMContext):
    try:
        quan = int(msg.text)
        DBS.SetQuantity(DBS, quan)
        await state.finish()
        await msg.reply("✅")
        await msg.answer("👇 Выбирайте меню", reply_markup=admin_btn())
    except Exception as e:
        print(e)
        await msg.reply("Информация введена неверно. Пожалуйста, введите еще раз!")

# 


@dp.message_handler(text="Реферальная ссылка")
async def ReferralLink(msg: types.Message):
    await SateSetLink.road.set()
    await msg.answer("Отправьте линк", reply_markup=interview_btn)

@dp.message_handler(text="Создать", state=SateSetLink.road)
async def RLCreate(msg: types.Message):
    await SateSetLink.next()
    await msg.answer("Отправить мне сообщение")

@dp.message_handler(text="Видеть все", state=SateSetLink.road)
async def RLGetAll(msg: types.Message, state: FSMContext):
    await state.finish()
    data = DBS.GetAll(DBS, 4)
    for x in data:
        await dp.bot.copy_message(msg.from_id, x[2], x[1], reply_markup=delete_btn(x[0]))

@dp.message_handler(content_types=types.ContentTypes.ANY,state=SateSetLink.promis)
async def BotCreateInterview(msg: types.Message, state: FSMContext):
    _id = DBS.CreateInterview(DBS, msg.message_id, msg.from_id, 4)
    await state.update_data(interviewID=_id)
    await msg.reply("✅")
    await msg.answer("Введите интервал в секундах")
    await SateSetLink.next()

@dp.message_handler(state=SateSetLink.interval)
async def BotRLInterval(msg: types.Message, state: FSMContext):
    try: 
        data = await state.get_data()
        DBS.SetInterval(DBS, int(msg.text), data['interviewID'])
        await msg.reply("✅")
        await msg.answer("👇 Выбирайте меню", reply_markup=admin_btn())
        await state.finish()
    except: 
        await msg.reply("Sifira qilip jiberin'")

 
# 


@dp.message_handler(text="Видео интервью с оснаветельом")
async def VideoInterview(msg: types.Message):
    await SateSetInterview.road.set()
    await msg.answer("👇 Выбирайте меню", reply_markup=interview_btn)

@dp.message_handler(text="Создать", state=SateSetInterview.road)
async def Create(msg: types.Message):
    await SateSetInterview.next()
    await msg.answer("Отправить мне сообщение")

@dp.message_handler(text="Видеть все", state=SateSetInterview.road)
async def VGetAll(msg: types.Message, state: FSMContext):
    await state.finish()
    data = DBS.GetAll(DBS, 1)
    if data:
        for x in data:
            await msg.reply("✅", reply_markup=back_btn)
            await dp.bot.copy_message(msg.from_id, x[2], x[1], reply_markup=delete_btn(x[0]))
    else:
        await msg.reply("Not Found", reply_markup=admin_btn())


@dp.message_handler(content_types=types.ContentType.ANY, state=SateSetInterview.promis)
async def BotCreateInterview(msg: types.Message, state: FSMContext):
    _id = DBS.CreateInterview(DBS, msg.message_id, msg.from_id, 1)
    await state.update_data(interviewID=_id)
    await msg.reply("✅")
    await msg.answer("Введите интервал в секундах")
    await SateSetInterview.next()

@dp.message_handler(state=SateSetInterview.interval)
async def BotCreateInterviewInterval(msg: types.Message, state: FSMContext):
    try: 
        data = await state.get_data()
        DBS.SetInterval(DBS, int(msg.text), data['interviewID'])
        await msg.reply("✅")
        await msg.answer("👇 Выбирайте меню", reply_markup=admin_btn())
        await state.finish()
    except: 
        await msg.reply("Sifira qilip jiberin'")
    
# 

@dp.message_handler(text="Рандомный пост")
async def RandomPost(msg: types.Message):
    await SateSetRandomPost.road.set()
    await msg.answer("👇 Выбирайте меню", reply_markup=interview_btn)

@dp.message_handler(text="Создать", state=SateSetRandomPost.road)
async def RCreate(msg: types.Message):
    await SateSetRandomPost.next()
    await msg.answer("Отправить мне сообщение")

@dp.message_handler(text="Видеть все", state=SateSetRandomPost.road)
async def RPGetAll(msg: types.Message, state: FSMContext):
    await state.finish()
    data = DBS.GetAll(DBS, 2)
    if data:
        for x in data:
            await msg.reply("✅", reply_markup=back_btn)
            await dp.bot.copy_message(msg.from_id, x[2], x[1], reply_markup=delete_btn(x[0]))
    else:
        await msg.reply("Not Found", reply_markup=admin_btn())


@dp.message_handler(content_types=types.ContentType.ANY, state=SateSetRandomPost.promis)
async def BotCreateRpost(msg: types.Message, state: FSMContext):
    _id = DBS.CreateInterview(DBS, msg.message_id, msg.from_id, 2)
    await state.update_data(interviewID=_id)
    await msg.reply("✅")
    await msg.answer("Введите интервал в секундах")
    await SateSetRandomPost.next()


@dp.message_handler(state=SateSetRandomPost.interval)
async def BotCreateRabdomPostInterval(msg: types.Message, state: FSMContext):
    try: 
        data = await state.get_data()
        DBS.SetInterval(DBS, int(msg.text), data['interviewID'])
        await msg.reply("✅")
        await msg.answer("👇 Выбирайте меню", reply_markup=admin_btn())
        await state.finish()
    except: 
        await msg.reply("Sifira qilip jiberin'")

#


@dp.message_handler(text="Пост о программе")
async def BotOprogr(msg: types.Message):
    await SateSetOprogram.road.set()
    await msg.answer("👇 Выбирайте меню", reply_markup=interview_btn)

@dp.message_handler(text="Создать", state=SateSetOprogram.road)
async def OPCreate(msg: types.Message):
    await SateSetOprogram.next()
    await msg.answer("Отправить мне сообщение")


@dp.message_handler(text="Видеть все", state=SateSetOprogram.road)
async def POGetAll(msg: types.Message, state: FSMContext):
    await state.finish()
    data = DBS.GetAll(DBS, 3)
    if data:
        for x in data:
            await msg.reply("✅", reply_markup=back_btn)
            await dp.bot.copy_message(msg.from_id, x[2], x[1], reply_markup=delete_btn(x[0]))
    else:
        await msg.reply("Not Found", reply_markup=admin_btn())

@dp.message_handler(content_types=types.ContentType.ANY, state=SateSetOprogram.promis)
async def BotCreateOProgram(msg: types.Message, state: FSMContext):
    _id = DBS.CreateInterview(DBS, msg.message_id, msg.from_id, 3)
    await state.update_data(interviewID=_id)
    await msg.reply("✅")
    await msg.answer("Введите интервал в секундах")
    await SateSetOprogram.next()

@dp.message_handler(state=SateSetOprogram.interval)
async def BotCreateOPInterval(msg: types.Message, state: FSMContext):
    try: 
        data = await state.get_data()
        DBS.SetInterval(DBS, int(msg.text), data['interviewID'])
        await msg.reply("✅")
        await msg.answer("👇 Выбирайте меню", reply_markup=admin_btn())
        await state.finish()
    except: 
        await msg.reply("Sifira qilip jiberin'")


@dp.callback_query_handler(lambda call: call.data.startswith('del='))
async def deleteFunc(call: types.CallbackQuery):
    _id = call.data.split('=')[1]
    DBS.post_sql_query(f"DELETE FROM Send WHERE id={_id}")
    await call.message.delete()
    