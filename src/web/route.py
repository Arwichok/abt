import secrets
from typing import Union


from pydantic import BaseModel
from fastapi import APIRouter, Depends as D, Header, Request, Form, Path, HTTPException
from fastapi.responses import RedirectResponse
from aiogram import Dispatcher, Bot, types

from ..util.service import Service
from ..util import config



class Route:
    def __init__(self, service: Service):
        self.rt = APIRouter()
        self.rt.get("/")(self.root)
        self.rt.post("/bot_wh/{token}")(self.bot_wh)
        self.service = service

    async def root(self):
        return dict(d=self.service.ct.tg.bot.token)
    
    async def bot_wh(
        self,
        update: types.Update,
        token: str,
        x_telegram_bot_api_secret_token: Union[str, None] = Header(default=None)
    ):
        if secrets.compare_digest(x_telegram_bot_api_secret_token, config.TELEGRAM_SECRET):
            if secrets.compare_digest(token, config.TELEGRAM_BOT_TOKEN):
                await self.service.ct.tg.feed_webhook_update(update)
                return True
        else:
            raise HTTPException(status_code=403)





# @rt.get("/", response_class=RedirectResponse)
# async def redirect():
#     return "/static/setup.html"

# @rt.get("/api")
# async def api():
#     return {"hello": "data"}

# @rt.post("/bot_wh/{token}")
# async def bot_wh(update: Update, token: str, x_telegram_bot_api_secret_token: Union[str, None] = Header(default=None)):
    

# @rt.post("/bot/setup")
# async def bot_setup(token: str = Form(), dp: Dispatcher = D()):
#     if secrets.compare_digest(token, config.TELEGRAM_BOT_TOKEN):
        
#         return dict(ok=True)
#     return dict(ok=False)


# @rt.post("/bot/webhook")
# async def bot_webhook():
#     ...