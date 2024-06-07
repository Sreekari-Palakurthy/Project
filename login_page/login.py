from fastapi import FastAPI, Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class user(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True,)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    password = Column(String)


Base.metadata.create_all(bind=engine)

app = FastAPI()


class userdata(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str


@app.post("/loginpage")
async def loginpage_user(user_data: userdata):
    db = SessionLocal()
    db_loginpage = user(first_name=user_data.first_name, last_name=user_data.last_name, username=user_data.username, password=user_data.password)
    db.add(db_loginpage)
    db.commit()
    db.refresh(db_loginpage)
    return db_loginpage



