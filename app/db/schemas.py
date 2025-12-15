from pydantic import BaseModel

class UpdateCategory(BaseModel):
    keyword: str
    category: str