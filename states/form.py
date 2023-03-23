from aiogram.dispatcher.filters.state import State, StatesGroup

class SetTime(StatesGroup):
    promis = State()
    senMSG = State()