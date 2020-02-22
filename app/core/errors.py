from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

ACCESS_DENIED_ERROR = HTTPException(HTTP_401_UNAUTHORIZED, detail="This entry does not belong to the logged in user")

INVALID_CREDENTIALS_ERROR = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="Invalid credentials",
    headers={"WWW-Authenticate": "Bearer"}
)


class NotAuthenticatedError(Exception):
    pass
