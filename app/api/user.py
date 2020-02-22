from fastapi import APIRouter, Depends, HTTPException

from app.core.security import manager
from app.db.base import get_db
from app import crud
from app import schemas
from app.schemas import Token

router = APIRouter()


@router.post('/register', response_model=schemas.UserRegistered, status_code=201)
def register(user: schemas.UserCreate, db=Depends(get_db)):
    if crud.user.get(user.email, db):
        raise HTTPException(
            409, 'A User with this email already exists'
        )
    user = schemas.User.from_orm(crud.user.create(db, user))

    # create token
    access_token = manager.create_access_token(
        data={'sub': user.email}
    )
    token = Token(access_token=access_token, token_type="Bearer")
    return schemas.UserRegistered(**user.dict(), login_credentials=token)
