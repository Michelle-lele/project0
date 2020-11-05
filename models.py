from sqlalchemy import Integer, Column, String
from sqlalchemy.types import Date, DateTime
from sqlalchemy_utils import force_auto_coercion, EmailType
from database import Base, engine
import datetime

force_auto_coercion()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String(30), nullable=False)
	email = Column(EmailType(length=255), unique=True, nullable=False)
	password = Column(String(200), nullable=False)
	registered_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)