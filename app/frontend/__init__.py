from pathlib import Path

from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles


FRONTEND_DIR = Path(__file__).parent
frontend_server = FastAPI()


static_server = StaticFiles(directory=str(FRONTEND_DIR / 'static'))
templates = Jinja2Templates(str(FRONTEND_DIR / 'templates'))


@frontend_server.get('/')
@frontend_server.get('/{path}')  # redirect all calls to the preact frontend
def index(request: Request, path: str = None):
    return templates.TemplateResponse(
        'index.html',
        {'request': request}
        )
