from fastapi import Request


class TestMiddelware:

    async def __call__(self, request: Request, call_next):
        print(f"Request: {request.base_url.hostname}{request.url.path}")
        response = await call_next(request)
        print(f"Finish: {request.base_url.hostname}{request.url.path}")
        return response
