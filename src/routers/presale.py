from aiogram import Router, types, F
from aiogram.exceptions import TelegramBadRequest

from src.keyboards import presale as presale_kb
from src.lexicons import presale as presale_text


router = Router(name=__name__)


@router.callback_query(F.data == 'presale')
async def process_presale_action(
    callback: types.CallbackQuery,
):
    try:
        await callback.message.edit_text(
            text=presale_text.text_dict['main_text'],
            reply_markup=await presale_kb.create_presale_kb()
        )
        await callback.answer()
    except TelegramBadRequest as e:
        if "message is not modified" in str(e):
            pass
        else:
            raise e
    await callback.answer()
