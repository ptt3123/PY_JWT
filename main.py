# app run here
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager

from Service.RequestLimitService import RequestLimitByIPService
from Api import router
from config import settings


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    print("Server open...")

    yield
    print("Server close...")


app = FastAPI(
    lifespan=lifespan,
)

app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)

app.include_router(router)


request_limit_by_ip_service = RequestLimitByIPService(
    settings.MAX_REQUEST_PER_IP, settings.MINUTES_LOCK_REQUEST_PER_IP)


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    ip = request.headers.get("X-Forwarded-For", request.client.host)

    if not await request_limit_by_ip_service.check(ip):
        return JSONResponse(
            status_code=429,
            content={"message": "Too many requests. Please try again later."},
            headers={"Retry-After": f"{settings.MINUTES_LOCK_REQUEST_PER_IP} minutes."},
        )

    response = await call_next(request)
    return response