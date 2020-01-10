from fastapi import HTTPException

ACCESS_DENIED_ERROR = HTTPException(401, detail="This entry does not belong to the logged in user")


class NotAuthenticatedError(Exception):
    pass
