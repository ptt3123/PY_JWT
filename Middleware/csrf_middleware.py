from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from itsdangerous import URLSafeTimedSerializer, BadSignature

from config import settings


# CSRFMiddleware
serializer = URLSafeTimedSerializer(settings.SECRET_KEY)


class CSRFMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        if request.method in ("POST", "PUT", "DELETE"):

            csrf_token = request.cookies.get("csrf_token")
            form_token = (await request.form()).get("csrf_token")

            if not csrf_token or not form_token:
                return JSONResponse(
                    status_code=503,
                    content={"message": "CSRF token missing."},
                )

            try:

                # Xác minh token
                serializer.loads(csrf_token)
                if csrf_token != form_token:
                    return JSONResponse(
                        status_code=503,
                        content={"message": "Invalid CSRF token."},
                    )

            except BadSignature:
                return JSONResponse(
                    status_code=503,
                    content={"message": "Invalid CSRF token."},
                )

        return await call_next(request)