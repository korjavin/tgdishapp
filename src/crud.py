from sqlalchemy.orm import Session
from . import database, schemas
from datetime import date

def get_user(db: Session, user_id: int):
    return db.query(database.User).filter(database.User.id == user_id).first()

def get_user_by_telegram_id(db: Session, telegram_id: int):
    return db.query(database.User).filter(database.User.telegram_id == telegram_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = database.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_duties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.Duty).offset(skip).limit(limit).all()

def get_duties_by_month(db: Session, year: int, month: int):
    start_date = date(year, month, 1)
    end_date = date(year, month + 1, 1) if month < 12 else date(year + 1, 1, 1)
    return db.query(database.Duty).filter(database.Duty.date >= start_date, database.Duty.date < end_date).all()

def create_duty(db: Session, duty: schemas.DutyCreate):
    db_duty = database.Duty(**duty.dict())
    db.add(db_duty)
    db.commit()
    db.refresh(db_duty)
    return db_duty
