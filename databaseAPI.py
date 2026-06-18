from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session

import pymysql
import os
import dotenv

from typing import Optional

dotenv.load_dotenv()
database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()

base.metadata.create_all(bind=engine)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

