from decimal import Decimal
from datetime import date

from pydantic import BaseModel, validator

from .base import ORMBase


class Expense(ORMBase):
    id: int
    value: Decimal
    date: date
    category: str


class ExpenseCreate(BaseModel):
    value: Decimal
    date: date
    category: str

    @validator('value')
    def positive_value(cls, v):
        if v < 0:
            raise ValueError("Value has to be positive!")
        return v
