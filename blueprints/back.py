from vkbottle.bot import Message

from vkbottle.bot import Blueprint

from utils.keyboard import MENU_KEYBOARD

bp = Blueprint()
bp.name = "Back"


@bp.on.message(payload={"cmd": "back"})
async def remove_status(message: Message):
    if message.state_peer:
        await bp.state_dispenser.delete(message.peer_id)

    await message.answer("Вернул", keyboard=MENU_KEYBOARD)
