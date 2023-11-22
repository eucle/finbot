from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Date, Integer, Numeric, String


class Base(DeclarativeBase):
    pass


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    subcategory = Column(String)
    payment_method = Column(String)
    amount = Column(Numeric(10, 2))
    created_at = Column(Date)
