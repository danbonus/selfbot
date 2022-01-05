import json
from models.status import Status

from datetime import datetime
from vkbottle.bot import Message
from vkbottle import Keyboard, Text

from vkbottle.bot import Blueprint

from utils.keyboard import MENU_KEYBOARD
from utils.states import StatusDeletionStates
from vkbottle import CtxStorage


bp = Blueprint()
bp.name = "Delete status"


@bp.on.message(text="Удалить статус из БД")
@bp.on.message(payload={"cmd": "delete_status"})
async def choose_status(message: Message):
    statuses = await Status.all()

    statuses_keyboard = Keyboard()

    for status in statuses:
        statuses_keyboard.add(Text(status.description, {"status_name": status.name}))

    await message.answer("Выбирай, епта", keyboard=statuses_keyboard.get_json())
    await bp.state_dispenser.set(message.peer_id, StatusDeletionStates.GET_STATUS)


@bp.on.message(state=StatusDeletionStates.GET_STATUS)
async def delete_status(message: Message):
    if not message.payload:
        await bp.state_dispenser.delete(message.peer_id)
        return "What the fuck are you talking about, bruv?"

    status_name = json.loads(message.payload)["status_name"]

    if f"status_{message.from_id}" in CtxStorage():
        if CtxStorage().get(f"status_{message.from_id}") == status_name:
            await bp.state_dispenser.delete(message.peer_id)
            return "Ты еблан? У тебя он щас стоит. Впрочем, у тебя ничего кроме статуса и не стоит."

    status = await Status.get(name=status_name)
    status_desc = status.description
    await message.answer(f"Статус <<{status_desc}>> удалён.", keyboard=MENU_KEYBOARD)
    await bp.state_dispenser.delete(message.peer_id)
    await status.delete()
