import secrets
from typing import Union

from pydantic import BaseModel
from fastapi import APIRouter, Depends as D, Request, Form
from fastapi.responses import RedirectResponse
from aiogram import Dispatcher, Bot

from ..util import config


rt = APIRouter()


@rt.get("/", response_class=RedirectResponse)
async def redirect():
    return "/static/setup.html"

@rt.get("/api")
async def api():
    return {"hello": "data"}

# @rt.post("/bot/setup")
# async def bot_setup(token: str = Form(), dp: Dispatcher = D()):
#     if secrets.compare_digest(token, config.TELEGRAM_BOT_TOKEN):
        
#         return dict(ok=True)
#     return dict(ok=False)


# @rt.post("/bot/webhook")
# async def bot_webhook():
#     ...