from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.team import Team
from app.schemas.team import TeamCreate, TeamUpdate, TeamResponse


router = APIRouter()


@router.get('/', response_model=List[TeamResponse])
def get_teams(db: Session = Depends(get_db)):
    return db.query(Team).all()


@router.get('/{team_id}', response_model=TeamResponse)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(404, 'Team not found')
    return TeamResponse.model_validate(team)


@router.post('/', response_model=TeamResponse, status_code=201)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    if db.query(Team).filter(Team.name == team.name).first():
        raise HTTPException(400, 'Team with this name already exists')
    db_team = Team(
        name=team.name,
        avatar_url=team.avatar_url or 'static/avatars/default.png'
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return TeamResponse.model_validate(db_team)


@router.put('/{team_id}', response_model=TeamResponse)
def update_team(team_id: int, team: TeamUpdate, db: Session = Depends(get_db)):
    db_team = db.query(Team).filter(Team.id == team_id).first()
    if not db_team:
        raise HTTPException(404, 'Team not found')
    if team.name is not None:
        if db.query(Team).filter(Team.name == team.name, Team.id != team_id).first():
            raise HTTPException(400, 'Team with this name already exists')
        db_team.name = team.name
    if team.avatar_url is not None:
        db_team.avatar_url = team.avatar_url
    db.commit()
    db.refresh(db_team)
    return TeamResponse.model_validate(db_team)


@router.delete('/{team_id}', status_code=204)
def delete_team(team_id: int, db: Session = Depends(get_db)):
    db_team = db.query(Team).filter(Team.id == team_id).first()
    if not db_team:
        raise HTTPException(404, 'Team not found')
    db.delete(db_team)
    db.commit()
    return None
