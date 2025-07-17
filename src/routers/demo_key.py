import logging
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest

from src.lexicons import presale as presale_text
from src.keyboards import start as start_kb
from src.services.xray_manager import XrayManager
from src.services.vpn_service import VPNService
from src.repositories.vpn_config import VPNConfigRepository
from src.repositories.user import UserRepository

router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.callback_query(F.data == 'demo-key')
async def process_in_development_action(
    callback: types.CallbackQuery,
):
    telegram_id = callback.message.chat.id
    username = callback.message.chat.username or str(telegram_id)
    logger.info(
        f"🔁 Обработка demo-key для пользователя: {telegram_id} (@{username})")

    try:
        xray = XrayManager()
        user_repo = UserRepository()
        vpn_repo = VPNConfigRepository()

        vpn_service = VPNService(
            xray=xray,
            user_repo=user_repo,
            vpn_repo=vpn_repo
        )

        try:
            vless_link = await vpn_service.create_vpn_user(
                telegram_id=telegram_id,
                label=username
            )
            logger.info(f"✅ Ключ выдан для {telegram_id}: {vless_link}")

            await callback.message.edit_text(
                text=(
                    f"{presale_text.text_dict['text_demo_key']}"
                    f"<code>{vless_link}</code>"
                    f"{presale_text.text_dict['text_instructions']}"
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=await start_kb.create_start_kb()
            )
            await xray.restart_xray()
        except ValueError as e:
            logger.warning(
                f"❌ Попытка повторной выдачи ключа для {telegram_id}: {str(e)}")
            await callback.answer(
                text=presale_text.text_dict['text_double_key'],
                show_alert=True
            )
        except Exception as e:
            await callback.answer(
                text=presale_text.text_dict['text_error_key'],
                show_alert=True
            )

            logger.exception(
                f"⚠️ Неизвестная ошибка при создании ключа для {telegram_id}")
    except TelegramBadRequest as e:
        if "message is not modified" in str(e):
            logger.debug(
                "Сообщение не было изменено, TelegramBadRequest подавлен")
        else:
            logger.exception("TelegramBadRequest")
            raise e
    except Exception as e:
        logger.exception(
            f"🚨 Общая ошибка при обработке demo-key для {telegram_id}")
    finally:
        await callback.answer()


@router.message(Command("reboot"))
async def process_in1_development_action(
    message: types.Message,
):
    xray = XrayManager()
    await xray.restart_xray()
    await message.answer("Xray перезапущен")
