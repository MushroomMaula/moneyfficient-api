from fastapi import APIRouter, Depends, HTTPException

from app import schemas
from app import crud
from app.core.security import manager, belongs_to_user
from app.db.base import get_db

router = APIRouter()


@router.post("/new", response_model=schemas.Expense, status_code=201)
def create(expense: schemas.ExpenseCreate, user=Depends(manager), db=Depends(get_db)):
    expense = crud.expense.create(expense, user.id, db)
    return expense


@router.get('/', response_model=schemas.ExpenseList, status_code=200)
def get_all(user=Depends(manager), db=Depends(get_db)):
    return {'data': crud.expense.get_by_user(user.id, db)}


@router.get('/{expense_id}', response_model=schemas.Expense, status_code=200)
def get(expense_id: int, user=Depends(manager), db=Depends(get_db)):
    expense = crud.expense.get(expense_id, db)
    belongs_to_user(expense, user)
    return expense


@router.put('/{expense_id}', status_code=204)
def edit(expense_id: int, data: schemas.ExpenseUpdate, user=Depends(manager), db=Depends(get_db)):
    expense = crud.expense.get(expense_id, db)
    belongs_to_user(expense, user)
    crud.expense.update(expense.id, data, db)


@router.delete('/{expense_id}', status_code=204)
def delete(expense_id: int, user=Depends(manager), db=Depends(get_db)):
    expense = crud.expense.get(expense_id, db)
    belongs_to_user(expense, user)
    crud.expense.delete(expense, db)
