from pydantic import BaseModel
from typing import Optional, List
from app.schemas.word import WordResponse


class PackBase(BaseModel):
    name: str
    description: Optional[str] = None


class PackCreate(PackBase):
    words: List[str] = []


class PackUpdate(PackBase):
    name: Optional[str] = None
    description: Optional[str] = None


class PackResponse(PackBase):
    id: int
    words: List[WordResponse] = []

    class Config:
        from_attributes = True
