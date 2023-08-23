from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:9898@localhost/forum.db'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session_local = sessionmaker(bind=engine)

Base = declarative_base()

from database.models import *


def get_db():
    db = Session_local()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
