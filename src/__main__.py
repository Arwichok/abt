import uvicorn

from .util import config

uvicorn.run("main:app", host=config.HOST, port=config.PORT)
