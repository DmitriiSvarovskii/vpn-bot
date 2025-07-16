from aiogram import Router, types, F
from aiogram.exceptions import TelegramBadRequest

from src.keyboards import help as help_kb
from src.lexicons import help as help_text


router = Router(name=__name__)


@router.callback_query(F.data == 'help')
async def process_help_action(
    callback: types.CallbackQuery,
):
    try:
        await callback.message.edit_text(
            text=help_text.text_dict['text_help'],
            reply_markup=await help_kb.create_help_kb()
        )
        await callback.answer()
    except TelegramBadRequest as e:
        if "message is not modified" in str(e):
            pass
        else:
            raise e
    await callback.answer()
