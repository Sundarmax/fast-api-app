from fastapi import Depends
from sqlalchemy.orm import session,sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread" : False})

sessionLocal = sessionmaker (
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

