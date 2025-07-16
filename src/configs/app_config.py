from .base import BaseConfig


class AppSettings(BaseConfig):
    PYTHONPATH: str
    DEBUG: bool
    BOT_TOKEN: str


app_settings = AppSettings()
