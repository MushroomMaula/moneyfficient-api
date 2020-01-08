from fastapi_login import LoginManager
from app.core import Config
from app.core.errors import ACCESS_DENIED_ERROR
from app.db_models.expense import Expense
from app.db_models.user import User

manager = LoginManager(Config.secret, tokenUrl='/auth/login')


def hash_password(plain_password):
    return manager.pwd_context.hash(plain_password)


def verify_password(plain_password, hashed_password):
    return manager.pwd_context.verify(plain_password, hashed_password)


def belongs_to_user(expense: Expense, user: User):
    if expense.owner_id == user.id:
        return True
    else:
        raise ACCESS_DENIED_ERROR
