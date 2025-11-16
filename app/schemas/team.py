from pydantic import BaseModel
from typing import Optional


class TeamBase(BaseModel):
    name: str
    avatar_url: Optional[str] = None


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    name: Optional[str] = None
    avatar_url: Optional[str] = None


class TeamResponse(TeamBase):
    id: int
    avatar_url: str

    class Config:
        from_attributes = True
