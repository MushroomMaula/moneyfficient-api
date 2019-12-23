from decimal import Decimal
from datetime import date

from pydantic import BaseModel

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
