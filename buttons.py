from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def source_btn():
    ikb = InlineKeyboardBuilder()
    instagram = InlineKeyboardButton(text="Instagramdan yuklash", callback_data='instagram')
    tiktok = InlineKeyboardButton(text="Tiktokdan yuklash", callback_data='tiktok')
    ikb.add(instagram, tiktok)
    ikb.adjust(1, repeat=True)
    return ikb.as_markup()
