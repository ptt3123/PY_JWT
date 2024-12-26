# app run here
from fastapi import FastAPI
from contextlib import asynccontextmanager

from Api import router


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    print("Server open...")

    yield
    print("Server close...")


app = FastAPI(
    lifespan=lifespan,
)


app.include_router(router)