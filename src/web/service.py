from dataclasses import dataclass, field
import pathlib

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import route


@dataclass
class WebService:
    app: FastAPI = field(init=False)
    
    def __post_init__(self):
        self.app = FastAPI()
        self.app.mount(
            path="/static", 
            app=StaticFiles(
                directory=pathlib.Path(__file__).parent.parent / "static", 
                html=True
            ), 
            name="static"
        )
        self.app.include_router(route.rt)
