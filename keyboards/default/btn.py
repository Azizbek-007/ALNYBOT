from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def admin_btn():
    text = ["Количество", "Реферальная ссылка", "Видео интервью с оснаветельом", "Рандомный пост", "Пост о программе"]
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    a = []
    for i in text:
        a.append(
        KeyboardButton(i))
    return markup.add(*a)
    
back_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("⬅️Назад"))

interview_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Видеть все"), KeyboardButton("Создать")).add("⬅️Назад") 