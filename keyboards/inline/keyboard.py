from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_btn(): 
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Send Message", callback_data="SendMessage")
    )