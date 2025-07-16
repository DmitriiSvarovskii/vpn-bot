__all__ = ("main_router",)

from aiogram import Router

from src.routers import start
from src.routers import presale
from src.routers import help
from src.routers import notification
from src.routers import demo_key
from src.routers import my_key
from src.routers import education


main_router = Router(name=__name__)

main_router.include_routers(
    start.router,
    presale.router,
    help.router,
    notification.router,
    demo_key.router,
    my_key.router,
    education.router,
)
