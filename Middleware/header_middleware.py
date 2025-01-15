from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class HeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        # Add header Referrer-Policy
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response