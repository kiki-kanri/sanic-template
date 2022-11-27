from sanic import HTTPResponse, Request


class ExampleMiddleware:
    def request(request: Request):
        print(request)

    def response(request: Request, response: HTTPResponse):
        print(response)
