from typing import Any

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsNumber(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool:
        user_input = message.text.split('.')

        if message.text.isdigit() or (
            len(user_input) == 2 and
            user_input[0].isdigit() and
            user_input[1].isdigit()
        ):
            return True
        return False


class IsAdmin(BaseFilter):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.user_id
