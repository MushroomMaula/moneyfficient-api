from .auth import Token
from .base import ORMBase
from pydantic import BaseModel


class User(ORMBase):
    id: str
    email: str
    username: str


class UserRegistered(User):
    login_credentials: Token


class UserCreate(BaseModel):
    email: str
    username: str
    password: str
