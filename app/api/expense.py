from fastapi import APIRouter, Depends, HTTPException

from app import schemas
from app import crud
from app.core.security import manager
from app.db.base import get_db

router = APIRouter()


@router.post("/new", response_model=schemas.Expense, status_code=201)
def create(expense: schemas.ExpenseCreate, user=Depends(manager), db=Depends(get_db)):
    expense = crud.expense.create(expense, user.id, db)
    return expense


@router.get('/', response_model=schemas.ExpenseList)
def get_all(user=Depends(manager), db=Depends(get_db)):
    return {'data': crud.expense.get_by_user(user.id, db)}


@router.get('/{expense_id}', response_model=schemas.Expense)
def get(expense_id: int, user=Depends(manager), db=Depends(get_db)):
    expense = crud.expense.get(expense_id, db)
    if expense.owner_id != user.id:
        raise HTTPException(401, detail="This entry does not belong to the logged in user")
    return expense