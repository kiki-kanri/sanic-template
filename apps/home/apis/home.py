from sanic import Blueprint, Request, text


home_api = Blueprint('home_api')


@home_api.get('/')
async def home(rq: Request):
    return text('Hello World!')
