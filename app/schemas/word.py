from pydantic import BaseModel


class WordBase(BaseModel):
    text: str


class WordCreate(WordBase):
    pass


class WordResponse(WordBase):
    id: int
    pack_id: int

    class Config:
        from_attributes = True
