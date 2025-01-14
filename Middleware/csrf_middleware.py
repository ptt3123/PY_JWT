from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from Dependency.ServiceDependency import csrf_token_service


class CSRFMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        if request.method in ("POST", "PUT", "DELETE"):

            csrf_token = request.cookies.get("csrf_token")
            form_token = (await request.form()).get("csrf_token")

            if not csrf_token or not form_token:
                return JSONResponse(
                    status_code=404,
                    content={"message": "CSRF token missing."},
                )

            if ((csrf_token != form_token) or
                    (not await csrf_token_service.verify_csrf_token(csrf_token))):

                return JSONResponse(
                    status_code=400,
                    content={"message": "Invalid CSRF token."},
                )

        return await call_next(request)