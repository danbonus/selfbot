import json
from models.status import Status

from datetime import datetime
from vkbottle.bot import Message
from vkbottle import Keyboard, Text

from vkbottle.bot import Blueprint

from utils.keyboard import MENU_KEYBOARD
from utils.states import SetStatusStates
from vkbottle import CtxStorage


bp = Blueprint()
bp.name = "Set status"


@bp.on.message(text="Установить статус")
@bp.on.message(payload={"cmd": "set_status"})
async def set_status(message: Message):
    statuses = await Status.all()

    statuses_keyboard = Keyboard()

    for status in statuses:
        statuses_keyboard.add(Text(status.description, {"status_name": status.name}))

    await message.answer("Выбирай, епта", keyboard=statuses_keyboard.get_json())
    await bp.state_dispenser.set(message.peer_id, SetStatusStates.GET_STATUS)


@bp.on.message(state=SetStatusStates.GET_STATUS)
async def get_status(message: Message):
    if not message.payload:
        await bp.state_dispenser.delete(message.peer_id)
        return "What the fuck are you talking about, bruv?"

    status_name = json.loads(message.payload)["status_name"]

    print("Status changed")
    CtxStorage().set(f"status_{message.from_id}", status_name)

    status_text = await Status.get(name=status_name).values("text")
    await message.answer(f"Статус изменён: {status_text['text']}", keyboard=MENU_KEYBOARD)
    await bp.state_dispenser.delete(message.peer_id)
