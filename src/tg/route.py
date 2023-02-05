from aiogram import Router, types
from aiogram.filters.command import CommandStart

from ..util.txt import TXT

rt = Router()


@rt.message(CommandStart())
async def start(message: types.Message):
    await message.answer(TXT.START_MESSAGE)
