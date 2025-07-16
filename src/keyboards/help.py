from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.lexicons import help


async def create_help_kb():
    keyboard = InlineKeyboardBuilder()

    help_btn = help.create_help_btn()

    for key, value in help_btn.items():
        if 'callback_data' in value:
            button = InlineKeyboardButton(
                text=value['text'],
                callback_data=value['callback_data']
            )
        elif 'url' in value:
            button = InlineKeyboardButton(
                text=value['text'],
                url=value['url']
            )
        else:
            continue

        keyboard.row(button)

    return keyboard.as_markup()
