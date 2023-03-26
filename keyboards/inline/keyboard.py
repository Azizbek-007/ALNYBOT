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

def added_btn(): 
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Odam qoshdim", callback_data="added")
    )