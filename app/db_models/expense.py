from sqlalchemy import Integer, Column, Numeric, Date, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from app.db.base import Base


class Expense(Base):
    id = Column(Integer, primary_key=True)
    value = Column(Numeric)
    date = Column(Date)
    created_on = Column(DateTime, server_default=now())
    category = Column(String(32))
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="expenses")
