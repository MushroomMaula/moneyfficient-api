from typing import Callable, List

import pytest
from starlette.testclient import TestClient

from app.core.security import manager
from app.db_models.expense import Expense
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
def user_data_factory() -> Callable:
    def f() -> schemas.UserCreate:
        return schemas.UserCreate(
            username=fake.user_name(),
            email=fake.email(),
            password=random_string()
        )
    return f


@pytest.fixture()
def expense_data_factory() -> Callable:
    def f() -> schemas.ExpenseCreate:
        return schemas.ExpenseCreate(
            value=random_float(),
            date=fake.date_object(),
            category=fake.random_element(elements=["Food", "Drink", "Gas", "Gift"])
        )
    return f


@pytest.fixture(scope='function')
def db_user_factory(user_data_factory, db) -> Callable:
    def f() -> User:
        user = crud.user.create(db, user_data_factory())
        return user
    return f


@pytest.fixture()
def db_expense_factory(db, expense_data_factory) -> Callable:
    def f(n, user) -> List[Expense]:
        expenses = []
        for i in range(n):
            data = expense_data_factory()
            expense = crud.expense.create(data, user.id, db)
            expenses.append(expense)
        return expenses
    return f


@pytest.fixture()
def access_headers(db_user_factory):
    user = db_user_factory()
    token = manager.create_access_token(
        data=dict(sub=user.email)
    )
    header = {'Authorization': f"Bearer {token}"}
    return user, header
