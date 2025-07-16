from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.lexicons import start


async def create_start_kb():
    keyboard = InlineKeyboardBuilder()

    start_btn = start.create_start_btn()

    for key, value in start_btn.items():
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
