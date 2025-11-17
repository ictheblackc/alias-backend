from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.settings import Settings
from app.schemas.settings import (
    SettingsCreate,
    SettingsUpdate,
    SettingsResponse,
)


router = APIRouter()


@router.get('/', response_model=List[SettingsResponse])
def get_settings(db: Session = Depends(get_db)):
    return db.query(Settings).all()


@router.post('/', response_model=SettingsResponse, status_code=201)
def create_settings(settings: SettingsCreate, db: Session = Depends(get_db)):
    if db.query(Settings).first():
        raise HTTPException(400, 'Settings already exist')
    db_settings = Settings(
        time_per_round=settings.time_per_round,
        win_score=settings.win_score,
        difficulty=settings.difficulty,
    )
    db.add(db_settings)
    db.commit()
    db.refresh(db_settings)
    return SettingsResponse.model_validate(db_settings)


@router.patch('/', response_model=SettingsResponse)
def update_settings(
    settings_id: int,
    settings: SettingsUpdate,
    db: Session = Depends(get_db)
):
    db_settings = db.query(Settings).filter(Settings.id == settings_id).first()
    if not db_settings:
        raise HTTPException(404, 'Settings not found')
    if settings.time_per_round is not None:
        db_settings.time_per_round = settings.time_per_round
    if settings.win_score is not None:
        db_settings.win_score = settings.win_score
    if settings.difficulty is not None:
        db_settings.difficulty = settings.difficulty
    db.commit()
    db.refresh(db_settings)
    return SettingsResponse.model_validate(db_settings)
