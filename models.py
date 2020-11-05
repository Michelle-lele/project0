from sqlalchemy import Integer, Column, String
from sqlalchemy.types import Date, DateTime
from database import Base, engine
import datetime

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String(30))
	password = Column(String)
	registered_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)