from sanic import Blueprint, Request, text


example_api = Blueprint('example_api')


@example_api.get('/')
async def example(request: Request):
    return text('Hello World!')
