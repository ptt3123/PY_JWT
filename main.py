# app run here
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager

from Service.RateLimitService import RateLimitService
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


server_rate_limit_service = RateLimitService(
    settings.MAX_REQUEST_PER_WINDOW, settings.MINUTES_PER_WINDOW)


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    if not await server_rate_limit_service.check_if_can_execute_request():
        return JSONResponse(
            status_code=503,
            content={"message": "Server is busy. Try again later."},
        )

    response = await call_next(request)
    return response