from fastapi import APIRouter, Depends

from Dependency.EndpointDependency import validate_jwt


info_router = APIRouter()


@info_router.get("/info")
async def info(data = Depends(validate_jwt)):
    return data