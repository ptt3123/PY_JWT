# app run here
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager

from Service.RateLimitService import RateLimitBaseService
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


server_rate_limit_service = RateLimitBaseService(
    settings.MAX_REQUEST_PER_WINDOW, settings.SECONDS_PER_WINDOW
)


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):

    x_forwarded_for = request.headers.get("x-forwarded-for")
    client_ip = x_forwarded_for.split(",")[0] if x_forwarded_for else request.client.host
    request.state.client_ip = client_ip

    if not await server_rate_limit_service.check():
        return JSONResponse(
            status_code=503,
            content={"message": "Server is busy. Try again later."},
        )

    response = await call_next(request)
    return response