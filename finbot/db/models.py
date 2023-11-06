from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime, Float, Integer, String


# Создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass


# Создаем модель, объекты которой будут храниться в БД
class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    subcategory = Column(String)
    payment_method = Column(String)
    amount = Column(Float)
    created_at = Column(DateTime)
