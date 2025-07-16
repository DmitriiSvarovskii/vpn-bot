from aiogram import Router, types, F

from src.lexicons import notification as notification_text


router = Router(name=__name__)


@router.callback_query(F.data == 'in-development')
async def process_in_development_action(
    callback: types.CallbackQuery,
):
    await callback.answer(
        text=notification_text.text_dict['in_development'],
        show_alert=True,
    )
    await callback.answer()


@router.callback_query(F.data == 'dont-sale')
async def process_dont_sale_action(
    callback: types.CallbackQuery,
):
    await callback.answer(
        text=notification_text.text_dict['dont_sale'],
        show_alert=True,
    )
    await callback.answer()
