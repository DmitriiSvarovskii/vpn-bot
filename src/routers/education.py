from aiogram import Router, types, F
from aiogram.exceptions import TelegramBadRequest

from src.keyboards import education as education_kb
from src.lexicons import education as education_lex


router = Router(name=__name__)


@router.callback_query(F.data == 'education')
async def process_education_action(
    callback: types.CallbackQuery,
):
    try:
        await callback.message.edit_text(
            text=education_lex.text_dict['text_instructions'],
            reply_markup=await education_kb.create_education_kb()
        )
        await callback.answer()
    except TelegramBadRequest as e:
        if "message is not modified" in str(e):
            pass
        else:
            raise e
    await callback.answer()
