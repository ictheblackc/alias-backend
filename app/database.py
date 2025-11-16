from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import Config as config

engine = create_engine(config.DATABASE_URL)

Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
