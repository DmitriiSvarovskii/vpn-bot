# from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import insert, select

from src.db.postgres import get_async_session
from src.models import User
from src.schemas.user import UserCreate


class UserRepository:
    """Класс для работы с таблицей users."""

    @staticmethod
    async def get_user_by_id(telegram_id: int) -> User:
        """
        Получает пользователея по user_id из базы данных.

        :return: Объект пользователя.
        :raises SQLAlchemyError: При ошибках взаимодействия с базой данных.
        """
        async for session in get_async_session():
            try:
                stmt = select(User).filter_by(telegram_id=telegram_id)
                result = await session.execute(stmt)
                user = result.scalar_one_or_none()
                return user
            except SQLAlchemyError as e:
                raise e

    @staticmethod
    async def crud_create_customer(
        data: UserCreate,
    ):
        async for session in get_async_session():
            try:
                stmt = (
                    insert(User).
                    values(**data.model_dump())
                )
                await session.execute(stmt)
                await session.commit()
                return {"status": 201}
            except SQLAlchemyError as e:
                raise e
