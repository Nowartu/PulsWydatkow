from db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date, Text
from datetime import date


class BankRecord(Base):
    __tablename__ = "bank_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    date: Mapped[date] = mapped_column(Date, nullable=False)
    operation_type: Mapped[str] = mapped_column(String(250), nullable=False)
    value: Mapped[int] = mapped_column(Integer, nullable=True)

    title: Mapped[str] = mapped_column(String(500))
    description: Mapped[str] = mapped_column(Text)

    category: Mapped[str] = mapped_column(String(100), nullable=True)


class Categories(Base):
    __tablename__ = "categories"

    keyword: Mapped[str] = mapped_column(String(100), primary_key=True)

    category: Mapped[str] = mapped_column(String(100))