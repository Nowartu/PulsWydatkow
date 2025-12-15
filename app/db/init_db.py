from db.models import *
from services.categories import CATEGORIES
from db.base import Base
from db.session import engine, SessionLocal
from sqlalchemy import inspect


def init_database():
    """
    Creates database tables if not exist and adds default categories.
    :return:
    """
    if not inspect(engine).has_table("categories"):
        Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        for category, value in CATEGORIES.items():
            for key in value:
                db.add(Categories(
                    keyword=key,
                    category=category
                ))
        db.commit()
        db.close()