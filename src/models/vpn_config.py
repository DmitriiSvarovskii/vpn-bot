import datetime

from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.postgres import Base, intpk, created_at

if TYPE_CHECKING:
    from src.models.user import User


class VPNConfig(Base):
    __tablename__ = 'vpn_configs'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)
    uuid: Mapped[str] = mapped_column(
        String(36), unique=True, nullable=False, index=True)
    flow: Mapped[str] = mapped_column(default="xtls-rprx-vision")
    email: Mapped[str | None]
    created_at: Mapped[created_at]
    is_active: Mapped[bool] = mapped_column(server_default=text("true"))
    expires_at: Mapped[datetime.date | None]

    user: Mapped["User"] = relationship(back_populates="configs")

    def __repr__(self):
        return f"<VPNConfig {self.email} (uuid={self.uuid})>"
