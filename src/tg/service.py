import asyncio
from dataclasses import dataclass, field

from aiogram import Bot, Dispatcher, Router, types
from ..util.service import Service
from ..util import config
from .route import rt


async def set_webhook(bot: Bot):
    await bot.set_webhook(
        url=f"{config.WEBHOOK_URL}/{bot.token}",
        secret_token=config.TELEGRAM_SECRET
    )

async def _setup_webhook(token: str):
    bot = Bot(token)
    await set_webhook(bot)
    await bot.session.close()
    

@dataclass
class TelegramService(Service):
    dp: Dispatcher = field(init=False)

    def __post_init__(self):
        self.dp = Dispatcher()
        self.dp.include_router(rt)
        self.bot = Bot(config.TELEGRAM_BOT_TOKEN)

    def run_polling(self):
        self.dp.run_polling(self.bot)

    def setup_webhook(self):
        asyncio.run(_setup_webhook(config.TELEGRAM_BOT_TOKEN))

    async def feed_webhook_update(self, update: types.Update):
        return await self.dp.feed_webhook_update(self.bot, update)
    