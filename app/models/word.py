from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Word(Base):
    __tablename__ = 'words'

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        )
    text = Column(
        String,
        nullable=False,
        unique=True,
        )
    pack_id = Column(
        Integer,
        ForeignKey('packs.id'),
        nullable=False,
        )

    pack = relationship(
        'Pack',
        back_populates='words',
        )
