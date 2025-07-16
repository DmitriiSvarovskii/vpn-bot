from typing import TYPE_CHECKING

from sqlalchemy import BIGINT, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.postgres import (
    Base, intpk, created_at
)


if TYPE_CHECKING:
    from src.models.vpn_config import VPNConfig


class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    source: Mapped[str | None]
    created_at: Mapped[created_at]
    is_active: Mapped[bool] = mapped_column(server_default=text("true"))
    is_admin: Mapped[bool] = mapped_column(server_default=text("false"))

    configs: Mapped[list["VPNConfig"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return (
            f"User("
            f"id={self.id}, "
            f"telegram_id={self.telegram_id}, "
            f"first_name={self.first_name}, "
            f"last_name={self.last_name}, "
            f"username={self.username}, "
            f"source={self.source}, "
            f"created_at={self.created_at}, "
            f"is_active={self.is_active}, "
            f"is_admin={self.is_admin}"
            f")"
        )
