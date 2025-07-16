from .base import BaseConfig


class VPNSettings(BaseConfig):
    CONFIG_PATH: str
    PBK: str
    SID: str
    SNI: str
    DOMAIN: str
    FLOW: str


vpn_settings = VPNSettings()
