from fastapi import APIRouter, Depends

from app import schemas
from app import crud
from app.core.security import manager
from app.db.base import get_db

router = APIRouter()


@router.post("/new", response_model=schemas.Expense, status_code=201)
def create(expense: schemas.ExpenseCreate, user=Depends(manager), db=Depends(get_db)):
    expense = crud.expense.create(expense, user.id, db)
    return expense
