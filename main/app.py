from pathlib import Path
from sanic import Request, Sanic, text


ROOT = Path(__file__).resolve().parent.parent


def create_app():
    sanic_app = Sanic('SanicApp')
    sanic_app.update_config(ROOT / 'instance' / 'config.py')
    response = text('Hello World!')

    @sanic_app.get('/')
    async def hello_world(request: Request):
        return response

    return sanic_app
