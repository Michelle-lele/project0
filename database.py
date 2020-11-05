import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import 	declarative_base

if not os.getenv("DATABASE_URL"):
	raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"),echo=True)
db = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

#TO DO instantiate session