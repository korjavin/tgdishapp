from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from decouple import config

DATABASE_URL = config("DATABASE_URL", default="sqlite:///./duties.db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    username = Column(String, unique=True, index=True)

    duties = relationship("Duty", back_populates="user")


class Duty(Base):
    __tablename__ = "duties"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="duties")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
