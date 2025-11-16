from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base


class Pack(Base):
    __tablename__ = 'packs'

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        )
    name = Column(
        String,
        nullable=False,
        unique=True,
        )
    description = Column(
        String,
        nullable=True,
        )

    words = relationship(
        'Word',
        back_populates='pack',
        cascade='all, delete-orphan',
        )
