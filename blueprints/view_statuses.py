from vkbottle.bot import Message

from vkbottle.bot import Blueprint

from vkbottle import CtxStorage, Keyboard, Text

from models.status import Status
from utils.keyboard import MENU_KEYBOARD

bp = Blueprint()
bp.name = "View statuses"


@bp.on.message(text="Просмотреть статусы")
@bp.on.message(payload={"cmd": "view_statuses"})
async def remove_status(message: Message):
    statuses = await Status.all()
    msg = "Доступные статусы: \n\n"

    for status in statuses:
        msg += f"{status.description}: {status.text}\n\n"

    return msg
