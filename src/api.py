from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db
from typing import List

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_telegram_id(db, telegram_id=user.telegram_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Telegram ID already registered")
    return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/duties/", response_model=List[schemas.Duty])
def read_duties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    duties = crud.get_duties(db, skip=skip, limit=limit)
    return duties

@router.post("/duties/", response_model=schemas.Duty)
def create_duty(duty: schemas.DutyCreate, db: Session = Depends(get_db)):
    return crud.create_duty(db=db, duty=duty)

@router.get("/duties/{year}/{month}", response_model=List[schemas.Duty])
def read_duties_by_month(year: int, month: int, db: Session = Depends(get_db)):
    duties = crud.get_duties_by_month(db, year=year, month=month)
    return duties
