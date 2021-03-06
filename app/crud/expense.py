from typing import List

from sqlalchemy.orm import Session

from app import schemas
from app.db_models.expense import Expense


def get(expense_id: int, db: Session) -> Expense:
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    return expense


def get_by_user(owner_id: int, db: Session) -> List[Expense]:
    expenses = db.query(Expense).filter(Expense.owner_id == owner_id).all()
    return expenses


def create(expense_in: schemas.ExpenseCreate, owner_id: int, db: Session):
    expense = Expense(**expense_in.dict(), owner_id=owner_id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


def update(expense_id: int, expense_in: schemas.ExpenseUpdate, db: Session):
    status = db.query(Expense).filter(
        Expense.id == expense_id
    ).update(expense_in.dict(exclude_none=True))
    db.commit()
    return status


def delete(expense: Expense, db: Session):
    status = db.delete(expense)
    db.commit()
    return status
