import pathlib

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import route



def create_app():
    _app = FastAPI()
    _app.mount(
        path="/static", 
        app=StaticFiles(
            directory=pathlib.Path(__file__).parent.parent / "static", 
            html=True
        ), 
        name="static"
    )
    _app.include_router(route.rt)
    return _app
