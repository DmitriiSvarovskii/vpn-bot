from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.lexicons import presale


async def create_presale_kb():
    keyboard = InlineKeyboardBuilder()

    admin_menu_btn = presale.create_presale_btn()

    buttons = [
        InlineKeyboardButton(
            text=value['text'], callback_data=value['callback_data'])
        for key, value in admin_menu_btn.items()
    ]

    keyboard.row(*buttons, width=1)

    return keyboard.as_markup()
