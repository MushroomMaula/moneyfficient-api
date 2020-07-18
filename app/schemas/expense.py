from decimal import Decimal
from datetime import date
from typing import List, Optional

from pydantic import BaseModel, validator

from .base import ORMBase


class Expense(ORMBase):
    id: int
    name: str
    value: Decimal
    date: date
    category: str


class ExpenseCreate(BaseModel):
    value: Decimal
    date: date
    category: str

    @validator('value')
    def positive_value(cls, v):
        if int(v) < 0:
            raise ValueError("Value has to be positive!")
        return v


class ExpenseUpdate(ORMBase):
    value: Optional[Decimal]
    date: Optional[date]
    category: Optional[str]

    @validator('value')
    def positive_value(cls, v):
        if v is None:
            return v
        if v < 0:
            raise ValueError("Value has to be positive!")
        return v


class ExpenseList(ORMBase):
    data: List[Expense]
