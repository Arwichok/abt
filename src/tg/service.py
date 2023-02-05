import asyncio
from dataclasses import dataclass, field

from aiogram import Bot, Dispatcher, Router
from ..util.service import Service
from ..util import config


async def set_webhook(bot: Bot):
    await bot.set_webhook(
        url=f"{config.WEBHOOK_URL}/{bot.token}",
        secret_token=config.TELEGRAM_SECRET
    )


@dataclass
class TelegramService(Service):
    dp: Dispatcher = field(init=False)

    def __post_init__(self):
        self.dp = Dispatcher()
        self.bot = Bot(config.TELEGRAM_BOT_TOKEN)

    def run_polling(self):
        self.dp.run_polling(self.bot)
