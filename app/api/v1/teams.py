from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.team import Team
from app.schemas.team import TeamResponse


router = APIRouter()


@router.get('/', response_model=List[TeamResponse])
def get_teams(db: Session = Depends(get_db)):
    return db.query(Team).all()
