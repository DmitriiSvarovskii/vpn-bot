from aiogram import Router, types, F
from aiogram.exceptions import TelegramBadRequest

from src.repositories.vpn_config import VPNConfigRepository
from src.lexicons import my_key as my_key_lex
from src.keyboards import start as start_kb
from src.configs.vpn_config import vpn_settings


router = Router(name=__name__)

vpn_repo = VPNConfigRepository()


@router.callback_query(F.data == 'my-keys')
async def show_my_key(callback: types.CallbackQuery):
    configs = await vpn_repo.get_configs_by_telegram_id(callback.from_user.id)

    if not configs:
        await callback.answer(
            "🔑 У вас пока нет активных VPN-ключей.",
            show_alert=True
        )
        return

    config = configs[0]

    link = (
        f"vless://{config.uuid}@{vpn_settings.DOMAIN}:443"
        f"?flow={config.flow}&type=tcp&security=reality"
        f"&fp=random&sni={vpn_settings.SNI}&pbk={vpn_settings.PBK}"
        f"&sid={vpn_settings.SID}&spx=/#" + config.email
    )
    try:
        await callback.message.edit_text(
            f"{my_key_lex.text_dict['text_one_key']}"
            f"{my_key_lex.text_dict['text_demo_key']}"
            f"<code>{link}</code>"
            f"{my_key_lex.text_dict['text_instructions']}",
            reply_markup=await start_kb.create_start_kb()
        )

    except TelegramBadRequest as e:
        if "message is not modified" in str(e):
            pass
        else:
            raise e
    await callback.answer()
