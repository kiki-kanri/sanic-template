from sanic import HTTPResponse, Request


class DefaultMiddleware:
    def request(request: Request):
        pass

    def response(request: Request, response: HTTPResponse):
        pass
