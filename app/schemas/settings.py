from pydantic import BaseModel
from typing import Optional


class SettingsBase(BaseModel):
    time_per_round: int
    win_score: int
    difficulty: str


class SettingsCreate(SettingsBase):
    pass


class SettingsUpdate(SettingsBase):
    time_per_round: Optional[int] = None
    win_score: Optional[int] = None
    difficulty: Optional[str] = None


class SettingsResponse(SettingsBase):
    id: int

    class Config:
        from_attributes = True
