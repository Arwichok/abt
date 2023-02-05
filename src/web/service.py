from dataclasses import dataclass, field

from fastapi import FastAPI

from .app import create_app


@dataclass
class WebService:
    app: FastAPI = field(init=False)
    
    def __post_init__(self):
        self.app = FastAPI()
        app.mount(
            path="/static", 
            app=StaticFiles(
                directory=pathlib.Path(__file__).parent.parent / "static", 
                html=True
            ), 
            name="static"
        )
        app.include_router(route.rt)