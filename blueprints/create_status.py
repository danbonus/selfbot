import json
from models.status import Status

from datetime import datetime
from vkbottle.bot import Message
from vkbottle import Keyboard, Text

from vkbottle.bot import Blueprint

from utils.keyboard import MENU_KEYBOARD, BACK_TO_MENU
from utils.states import StatusCreationStates
from vkbottle import CtxStorage


bp = Blueprint()
bp.name = "Create status"


@bp.on.message(text="Создать статус")
@bp.on.message(payload={"cmd": "create_status"})
async def create_status(message: Message):
    await bp.state_dispenser.set(message.peer_id, StatusCreationStates.GET_NAME)
    await message.answer("Введи программное нзвание статуса.", keyboard=BACK_TO_MENU)


@bp.on.message(state=StatusCreationStates.GET_NAME)
async def get_name(message: Message):
    CtxStorage().set(f"{message.from_id}_status_name", message.text)
    await bp.state_dispenser.set(message.peer_id, StatusCreationStates.GET_DESCRIPTION)
    return "Ок, название получил. Ты спецом такое уебское придумал? Кринж.. бляяя. Вводи краткое описание."


@bp.on.message(state=StatusCreationStates.GET_DESCRIPTION)
async def get_description(message: Message):
    await bp.state_dispenser.set(message.peer_id, StatusCreationStates.GET_TEXT)

    CtxStorage().set(f"{message.from_id}_status_desc", message.text)
    return "Ага, теперь и эту хуйню записал. Пиздец, чем я занимаюсь на старость лет? " \
           "Вводи текст, который будут получать юзеры."


@bp.on.message(state=StatusCreationStates.GET_TEXT)
async def get_text(message: Message):
    status = await Status.create(
        name=CtxStorage().get(f"{message.from_id}_status_name"),
        description=CtxStorage().get(f"{message.from_id}_status_desc"),
        text=message.text
    )
    await bp.state_dispenser.delete(message.peer_id)
    return "Ну всё, блять, молодец. Создано."
