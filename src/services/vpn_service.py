from datetime import date, timedelta

from src.services.xray_manager import XrayManager
from src.repositories.vpn_config import VPNConfigRepository
from src.repositories.user import UserRepository
from src.schemas.vpn_config import VPNConfigCreate


class VPNService:
    def __init__(
        self,
        xray: XrayManager,
        vpn_repo: VPNConfigRepository,
        user_repo: UserRepository
    ):
        self.xray = xray
        self.vpn_repo = vpn_repo
        self.user_repo = user_repo

    async def create_vpn_user(self, telegram_id: int, label: str) -> str:
        """Создание VPN-пользователя (Xray + БД) по Telegram ID"""
        user = await self.user_repo.get_user_by_id(telegram_id)
        if not user:
            raise ValueError(
                f"Пользователь с telegram_id={telegram_id} не найден")

        xray_data = await self.xray.add_user_to_config(label)
        expires = date.today() + timedelta(days=30)

        vpn_config = VPNConfigCreate(
            user_id=user.id,
            uuid=xray_data["uuid"],
            flow=xray_data["flow"],
            email=xray_data["email"],
            expires_at=expires
        )

        await self.vpn_repo.create_vpn_config(vpn_config)
        return xray_data["vless_link"]
