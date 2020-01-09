from pathlib import Path

from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates


frontend_server = FastAPI()

templates = Jinja2Templates(str(Path(__file__).parent / 'templates'))


@frontend_server.get('/')
async def index(request: Request):
    print(templates.env)
    return templates.TemplateResponse('index.html', {'request': request})
