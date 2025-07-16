from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.lexicons import education


async def create_education_kb():
    keyboard = InlineKeyboardBuilder()

    education_btn = education.create_education_btn()

    for key, value in education_btn.items():
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
