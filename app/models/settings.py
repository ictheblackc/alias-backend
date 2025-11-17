from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Settings(Base):
    __tablename__ = 'settings'

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        )
    time_per_round = Column(
        Integer,
        default=60,
        )
    win_score = Column(
        Integer,
        default=50,
        )
    difficulty = Column(
        String,
        default='medium',
        )
