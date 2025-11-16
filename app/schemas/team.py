from pydantic import BaseModel
from typing import Optional


class TeamBase(BaseModel):
    name: str
    avatar_url: Optional[str] = None


class TeamCreate(TeamBase):
    pass


class TeamResponse(TeamBase):
    id: int
    avatar_url: str
