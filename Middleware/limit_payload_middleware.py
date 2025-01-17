from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class LimitPayloadMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        max_size = 10 * 1024 * 1024  # Giới hạn 10MB

        if int(request.headers.get("content-length", 0)) > max_size:
            return JSONResponse(content={"error": "Payload too large"}, status_code=413)

        return await call_next(request)