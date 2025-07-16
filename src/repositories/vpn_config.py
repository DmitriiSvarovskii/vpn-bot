# from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import insert, select

from src.db.postgres import get_async_session
from src.models import VPNConfig, User
from src.schemas.vpn_config import VPNConfigCreate


class VPNConfigRepository:
    """Класс для работы с таблицей users."""

    @staticmethod
    async def get_vpn_config_by_user_id(user_id: int) -> VPNConfig:
        """
        Получает vpn_config по user_id из базы данных.

        :return: Объект пользователя.
        :raises SQLAlchemyError: При ошибках взаимодействия с базой данных.
        """
        async for session in get_async_session():
            try:
                stmt = select(VPNConfig).where(user_id=user_id)
                result = await session.execute(stmt)
                vpn_config = result.scalar_one_or_none()
                return vpn_config
            except SQLAlchemyError as e:
                raise e

    @staticmethod
    async def get_configs_by_telegram_id(
        telegram_id: int
    ) -> list[VPNConfig]:
        async for session in get_async_session():
            stmt = (
                select(VPNConfig)
                .join(User)
                .where(User.telegram_id == telegram_id)
            )
            result = await session.execute(stmt)
            return result.scalars().all()

    @staticmethod
    async def create_vpn_config(
        data: VPNConfigCreate,
    ):
        async for session in get_async_session():
            try:
                stmt = (
                    insert(VPNConfig).
                    values(**data.model_dump())
                )
                await session.execute(stmt)
                await session.commit()
                return {"status": 201}
            except SQLAlchemyError as e:
                raise e
