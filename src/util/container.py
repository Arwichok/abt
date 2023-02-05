from dataclasses import dataclass, field
from typing import Dict
from aiogram import Bot, Dispatcher

from fastapi import FastAPI

from ..tg.factory import create_dp, create_bot
from ..web.app import create_app
from . import config


@dataclass
class Container:
    app: FastAPI = field(default_factory=create_app)
    dp: Dispatcher = field(default_factory=create_dp)
    bots: Dict[str, Bot] = field(default_factory=dict)

    def __post_init__(self):
        ...
