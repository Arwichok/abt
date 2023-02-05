from dataclasses import dataclass, field, fields

from .service import Service
from ..tg.service import TelegramService
from ..web.service import WebService


@dataclass
class Container:
    tg: TelegramService = field(default_factory=TelegramService)
    web: WebService = field(default_factory=WebService)
    
    def __post_init__(self):
        self.setup_services()

    def setup_services(self):
        for obj in fields(self):
            if isinstance(obj, Service):
                getattr(self, obj.name).ct = self

