import random
import asyncio

from vkbottle import load_blueprints_from_package
from vkbottle.user import User, Message, run_multibot
from vkbottle.bot import Bot
import asyncio
from vkbottle.api import API
import logging
import sys
from orm import init
from blueprints import bps
from vkbottle import CtxStorage
from models.status import Status
from middlewares.ThresholdMiddleware import ThresholdMiddleware
from vkbottle import LoopWrapper
from vkbottle.user import rules

logger = logging.getLogger("vkbottle")
logger.setLevel(20)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    u'[%(asctime)s] %(levelname)s: %(message)s ' + '(%(filename)s:%(threadName)s:%(funcName)s:%(lineno)s)',
    datefmt='%Y-%m-%d %H:%M:%S'
)
handler.setFormatter(formatter)
logger.addHandler(handler)

lw = LoopWrapper()
user = User()
user.loop_wrapper = lw
user.labeler.message_view.register_middleware(ThresholdMiddleware)
bot = Bot(token="")
bot.loop_wrapper = lw


@user.on.private_message(rules.FromUserRule())
async def hi_handler(message: Message):
    current_user = await message.ctx_api.account.get_profile_info()
    uid = current_user.id
    status = CtxStorage().get(f"status_{uid}")

    if status:
        status_text = await Status.get(name=status).values("text")

        users_info = await bot.api.users.get(message.from_id)
        await message.answer("Привет, {}.\n{}".format(users_info[0].first_name, status_text["text"]))


if __name__ == '__main__':
    storage = CtxStorage()
    for i in bps:
        i.load(bot)
    loop = asyncio.get_event_loop()
    lw.add_task(bot.run_polling())
    lw.add_task(init())
    run_multibot(
        user,
        apis=(
            API(token=""),
        )
    )
