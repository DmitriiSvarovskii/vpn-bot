import json

from uuid import uuid4
from pathlib import Path

from src.configs.vpn_config import vpn_settings


class XrayManager:
    def __init__(
        self,
        config_path: str = vpn_settings.CONFIG_PATH,
        pbk: str = vpn_settings.PBK,
        sid: str = vpn_settings.SID,
        sni: str = vpn_settings.SNI,
        domain: str = vpn_settings.DOMAIN,
        flow: str = vpn_settings.FLOW
    ):
        self.config_path = Path(config_path)
        self.pbk = pbk
        self.sid = sid
        self.sni = sni
        self.domain = domain
        self.flow = flow

    async def read_config(self) -> dict:
        with self.config_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    async def write_config(self, config: dict):
        with self.config_path.open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

    async def add_user_to_config(self, label: str) -> dict:
        if not label or len(label.strip()) < 2:
            raise ValueError("Метка не может быть пустой")

        uuid = str(uuid4())
        label += '-fast-rabbit-vpn🇩🇪'

        config = await self.read_config()

        for inbound in config.get("inbounds", []):
            if inbound.get("protocol") == "vless":
                clients = inbound["settings"]["clients"]

                if any(c.get("email") == label for c in clients):
                    raise ValueError(f"Пользователь '{label}' уже существует")

                clients.append({
                    "id": uuid,
                    "flow": self.flow,
                    "email": label
                })

        await self.write_config(config)

        vless_link = (
            f"vless://{uuid}@{self.domain}:443"
            f"?flow={self.flow}&type=tcp&security=reality"
            f"&fp=random&sni={self.sni}&pbk={self.pbk}&sid={self.sid}&spx=/#" + label
        )

        return {
            "uuid": uuid,
            "email": label,
            "flow": self.flow,
            "vless_link": vless_link
        }

    async def delete_user(self, label: str) -> bool:
        """
        Удаляет пользователя с указанной меткой (label).
        Возвращает True, если пользователь был удалён.
        """
        if not label or len(label.strip()) < 2:
            raise ValueError("Метка не может быть пустой")

        config = await self.read_config()
        deleted = False
        label += '-fast-rabbit-vpn🇩🇪'

        for inbound in config.get("inbounds", []):
            if inbound.get("protocol") == "vless":
                clients = inbound["settings"]["clients"]
                initial_len = len(clients)

                inbound["settings"]["clients"] = [
                    c for c in clients if c.get("email") != label
                ]

                if len(inbound["settings"]["clients"]) < initial_len:
                    deleted = True

        if not deleted:
            raise ValueError(f"Пользователь с меткой '{label}' не найден")

        await self.write_config(config)
        return True
