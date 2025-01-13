# app run here
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager

from Api import router
from Middleware import CSRFMiddleware, RateLimitMiddleware


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    print("Server open...")

    yield
    print("Server close...")


app = FastAPI(
    lifespan=lifespan,
)

app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)

# Custom Middleware
app.add_middleware(CSRFMiddleware)
app.add_middleware(RateLimitMiddleware)

app.include_router(router)