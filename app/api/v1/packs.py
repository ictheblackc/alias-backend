from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.pack import Pack
from app.models.word import Word
from app.schemas.pack import PackCreate, PackUpdate, PackResponse


router = APIRouter()


@router.get('/', response_model=List[PackResponse])
def get_packs(db: Session = Depends(get_db)):
    return db.query(Pack).all()


@router.get('/{pack_id}', response_model=PackResponse)
def get_pack(pack_id: int, db: Session = Depends(get_db)):
    pack = db.query(Pack).filter(Pack.id == pack_id).first()
    if not pack:
        raise HTTPException(404, 'Pack not found')
    return PackResponse.model_validate(pack)


@router.post('/', response_model=PackResponse, status_code=201)
def create_pack(pack: PackCreate, db: Session = Depends(get_db)):
    if db.query(Pack).filter(Pack.name == pack.name).first():
        raise HTTPException(400, 'Pack with this name already exists')
    db_pack = Pack(
        name=pack.name,
        description=pack.description,
    )
    db.add(db_pack)
    db.flush()
    for word in pack.words:
        new_word = Word(
            text=word,
            pack_id=db_pack.id,
        )
        db.add(new_word)
    db.commit()
    db.refresh(db_pack)
    return PackResponse.model_validate(db_pack)


@router.patch('/{pack_id}', response_model=PackResponse)
def update_pack(pack_id: int, pack: PackUpdate, db: Session = Depends(get_db)):
    db_pack = db.query(Pack).filter(Pack.id == pack_id).first()
    if not db_pack:
        raise HTTPException(404, 'Pack not found')
    if pack.name is not None:
        if db.query(Pack).filter(
            Pack.name == pack.name,
            Pack.id != pack_id,
        ).first():
            raise HTTPException(400, 'Pack with this name already exists')
        db_pack.name = pack.name
    db.commit()
    db.refresh(db_pack)
    return PackResponse.model_validate(db_pack)


@router.delete('/{pack_id}', status_code=204)
def delete_pack(pack_id: int, db: Session = Depends(get_db)):
    db_pack = db.query(Pack).filter(Pack.id == pack_id).first()
    if not db_pack:
        raise HTTPException(404, 'Pack not found')
    db.delete(db_pack)
    db.commit()
    return None
