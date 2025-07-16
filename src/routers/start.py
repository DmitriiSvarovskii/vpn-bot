from aiogram import Router, types, F
from aiogram.filters import CommandStart, CommandObject
from aiogram.exceptions import TelegramBadRequest
from sqlalchemy.exc import SQLAlchemyError

from src.keyboards import start
from src.lexicons import start as start_lex
from src.repositories.user import UserRepository
from src.schemas.user import UserCreate


router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(
    message: types.Message, command: CommandObject
):
    payload = command.args
    if message.chat.type == 'private':
        data = await UserRepository.get_user_by_id(
            telegram_id=message.from_user.id
        )
        try:
            if data:
                await message.answer(
                    text=start_lex.text_dict['text_repeat'],
                    reply_markup=await start.create_start_kb()
                )
            else:
                user_data = UserCreate(
                    telegram_id=message.from_user.id,
                    source=payload,
                    first_name=message.from_user.first_name,
                    last_name=message.from_user.last_name,
                    username=message.from_user.username
                )
                await UserRepository.crud_create_customer(data=user_data)
                await message.answer(
                    text=start_lex.text_dict['text_welcome'],
                    reply_markup=await start.create_start_kb()
                )

        except SQLAlchemyError as e:
            print(e)
            await message.answer(text="Произошла ошибка, пожалуйста повторите попытку. В случае, если ошибка повторится, пожалуйста обратитесь в support.")   # noqa


@router.callback_query(F.data == 'start')
async def process_start_action(
    callback: types.CallbackQuery,
):
    try:
        await callback.message.edit_text(
            text=start_lex.text_dict['text_repeat'],
            reply_markup=await start.create_start_kb()
        )
        await callback.answer()
    except TelegramBadRequest as e:
        if "message is not modified" in str(e):
            pass
        else:
            raise e
    await callback.answer()
