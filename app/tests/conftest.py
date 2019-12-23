import pytest
from starlette.testclient import TestClient

from app.core.security import manager
from app.db_models.user import User
from app.main import app
from app import schemas, crud
from app.tests.utils import fake, random_string, random_float
from app.db.base import create_all, SessionLocal, reset_db


@pytest.fixture(autouse=True)
def _():
    create_all()


@pytest.fixture(scope="session")
def db():
    db = SessionLocal()
    yield db
    db.close()
    # clear all tables
    reset_db()


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def user_data() -> schemas.UserCreate:
    return schemas.UserCreate(
        username=fake.user_name(),
        email=fake.email(),
        password=random_string()
    )


@pytest.fixture()
def expense_data() -> schemas.ExpenseCreate:
    return schemas.ExpenseCreate(
        value=random_float(),
        date=fake.date_object(),
        category=fake.random_element(elements=["Food", "Drink", "Gas", "Gift"])
    )


@pytest.fixture()
def db_user(user_data, db) -> User:
    user = crud.user.create(db, user_data)
    return user


@pytest.fixture()
def access_headers(db_user):
    token = manager.create_access_token(
        data=dict(sub=db_user.email)
    )
    header = {'Authorization': f"Bearer {token}"}
    return db_user, header
