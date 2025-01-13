from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from Service.RateLimitService import RateLimitBaseService
from config import settings


# RateLimitMiddleware
server_rate_limit_service = RateLimitBaseService(
    settings.MAX_REQUEST_PER_WINDOW, settings.SECONDS_PER_WINDOW
)


class RateLimitMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        x_forwarded_for = request.headers.get("x-forwarded-for")
        client_ip = x_forwarded_for.split(",")[0] if x_forwarded_for else request.client.host
        request.state.client_ip = client_ip

        if not await server_rate_limit_service.check():
            return JSONResponse(
                status_code=503,
                content={"message": "Server is busy. Try again later."},
            )

        return await call_next(request)