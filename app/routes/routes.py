from fastapi import APIRouter, UploadFile, Depends, HTTPException
from db.session import get_db
from db.models import Categories
from services.upload_file import upload_csv_file
from services.categories import categorize
from sqlalchemy import select
from db.schemas import UpdateCategory

api_router = APIRouter(
)

@api_router.post("/upload/")
def upload_file(file: UploadFile, db=Depends(get_db)):
    if file.filename.endswith(".csv"):
        if upload_csv_file(file.file, db):
            return "OK"
        else:
            raise HTTPException(400, detail="Nieobsługiwany typ pliku.")
    else:
        raise HTTPException(400, detail="Nieobsługiwany format pliku.")


@api_router.get("/categories/")
def get_categories(db=Depends(get_db)):
    return {x.keyword: x.category for x in db.execute(select(Categories)).scalars().all()}


@api_router.post("/categories/")
def update_or_create(uc: UpdateCategory, db=Depends(get_db)):
    keyword = db.execute(select(Categories).where(Categories.keyword == uc.keyword.upper())).scalar_one_or_none()
    if keyword is None:
        db.add(Categories(
            keyword=uc.keyword.upper(),
            category=uc.category.upper()
        ))
    else:
        keyword.category = uc.category.upper()
    db.commit()
    categorize(db)
    return "OK"

@api_router.delete("/categories/{keyword}")
def delete_categories(keyword: str, db=Depends(get_db)):
    keyword = db.execute(select(Categories).where(Categories.keyword == keyword)).scalar_one_or_none()
    if keyword is not None:
        db.delete(keyword)
        db.commit()
        categorize(db)
    return "OK"