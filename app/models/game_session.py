from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime


class GameSession(Base):
    __tablename__ = 'game_sessions'

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    started_at = Column(
        DateTime,
        default=datetime.now,
    )
    finished_at = Column(
        DateTime,
        nullable=True,
    )
    winner_team_id = Column(
        Integer,
        ForeignKey('teams.id'),
        nullable=True,
    )
    total_rounds = Column(
        Integer,
        default=0,
    )

    winner_team = relationship(
        'Team',
        foreign_keys=[winner_team_id],
    )
    team_scores = relationship(
        'TeamScore',
        back_populates='game_session',
        cascade="all, delete-orphan",
    )
