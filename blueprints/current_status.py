from vkbottle.bot import Message

from vkbottle.bot import Blueprint

from vkbottle import CtxStorage
from models.status import Status


bp = Blueprint()
bp.name = "Current status"


@bp.on.message(text="Текущий статус")
@bp.on.message(payload={"cmd": "show_status"})
async def remove_status(message: Message):
    status_name = CtxStorage().get(f"status_{message.from_id}")
    if not status_name:
        return 'А ничего и не стоит. Еблана кусок.'
    status_text = await Status.get(name=status_name).values("description")
    return f"Текущий статус: {status_text['description']}"
