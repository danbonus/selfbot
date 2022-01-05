from vkbottle import BaseMiddleware, CtxStorage
from vkbottle.bot import Message
import time
import asyncio
from models.status import Status

dummy_db = CtxStorage()


class ThresholdMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        if self.event.from_id == self.event.peer_id and self.event.from_id > 0:
            current_ts = time.time()
            if f"{self.event.from_id}_last_request_timestamp" in dummy_db:
                if current_ts - dummy_db.get(f"{self.event.from_id}_last_request_timestamp") < 500:

                    current_user = await self.event.ctx_api.account.get_profile_info()
                    uid = current_user.id

                    status = CtxStorage().get(f"status_{uid}")
                    status = await Status.get(name=status)

                    msg = await self.event.answer(
                        f"Статус: {status.description}\n\nТехническое сообщение. Пользователю не придут оповещения о том, что ты написал. Прочитает как только, так сразу."
                    )

                    await asyncio.sleep(5)
                    await self.event.ctx_api.messages.delete(message_ids=[msg], delete_for_all=True)

                    self.stop("Ебать он резвый.")

            dummy_db.set(f"{self.event.from_id}_last_request_timestamp", current_ts)
