from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.team import Team
from app.schemas.team import TeamCreate, TeamResponse


router = APIRouter()


@router.get('/', response_model=List[TeamResponse])
def get_teams(db: Session = Depends(get_db)):
    return db.query(Team).all()


@router.post('/', response_model=TeamResponse, status_code=201)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    new_team = Team(
        name=team.name,
        avatar_url=team.avatar_url or 'static/avatarts/default.png'
    )
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return TeamResponse.model_validate(new_team)
