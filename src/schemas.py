from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    telegram_id: int
    first_name: str
    last_name: str | None = None
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class DutyBase(BaseModel):
    date: date

class DutyCreate(DutyBase):
    user_id: int

class Duty(DutyBase):
    id: int
    user: User

    class Config:
        from_attributes = True
