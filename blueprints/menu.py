from vkbottle.bot import Message

from utils.keyboard import MENU_KEYBOARD

from vkbottle.bot import Blueprint
from vkbottle import CtxStorage


bp = Blueprint()
bp.name = "Menu"


@bp.on.private_message()
async def menu(message: Message):
    await message.answer("Вот клава.", keyboard=MENU_KEYBOARD)
