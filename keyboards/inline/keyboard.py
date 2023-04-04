from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_btn(): 
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Send Message 1", callback_data="SendMessage")
    ).add(
        InlineKeyboardButton(text="Send Message 2", callback_data="SendMessage2")
    ).add(
        InlineKeyboardButton(text="Send Message 3", callback_data="SendMessage3")
    ).add(
        InlineKeyboardButton(text="Send Message 4", callback_data="SendMessage4")
    )

def added_btn(user_id): 
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Я добавил", callback_data=f"added={user_id}")
    )

def delete_btn(cat_id):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("удалить", callback_data=f"del={cat_id}")
    )