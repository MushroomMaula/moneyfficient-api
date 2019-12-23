from sqlalchemy.orm import Session

from app import schemas
from app.db_models.expense import Expense
from app.db_models.user import User


def get(expense_id: int, db: Session) -> Expense:
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    return expense


def create(expense_in: schemas.ExpenseCreate, owner_id: int, db: Session):
    expense = Expense(**expense_in.dict(), owner_id=owner_id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense
