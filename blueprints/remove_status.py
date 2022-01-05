from vkbottle.bot import Message

from vkbottle.bot import Blueprint

from vkbottle import CtxStorage

from utils.keyboard import MENU_KEYBOARD

bp = Blueprint()
bp.name = "Remove status"


@bp.on.message(text="Удалить статус")
@bp.on.message(payload={"cmd": "remove_status"})
async def remove_status(message: Message):
    if not CtxStorage().get(f"status_{message.from_id}"):
        return "Что-что удалить? У тебя ничего не стоит, долбоёб!"

    await message.answer("Статус удалён, чмоша!")
    CtxStorage().delete(f"status_{message.from_id}")
