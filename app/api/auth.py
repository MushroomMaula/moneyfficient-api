from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.errors import INVALID_CREDENTIALS_ERROR
from app.core.security import manager, verify_password
from app import crud
from app.db.base import get_db

router = APIRouter()


@router.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    email = data.username
    password = data.password
    user = crud.user.get(email, db)
    if not user:
        raise INVALID_CREDENTIALS_ERROR
    elif not verify_password(password, user.password):
        raise INVALID_CREDENTIALS_ERROR

    access_token = manager.create_access_token(
        data={'sub': user.email}
    )
    return {'access_token': access_token, 'token_type': 'Bearer'}



