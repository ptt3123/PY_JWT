from fastapi import HTTPException, status

USER_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User Not Found!!!",
)

METHOD_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Method Not Found!!!",
)

TOO_MUCH_LOGIN_REQUEST_EXCEPTION = HTTPException(
    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
    detail="Too Much Login Request!!!",
)

REFRESH_TOKEN_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Refresh Token Not Found!!!"
)

DATABASE_EXCEPTION = HTTPException(
    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
    detail="Connection Error. Please Try Again Later!!!"
)

EXPIRED_TOKEN = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token has expired!!!"
)

INVALID_TOKEN = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token!!!"
)