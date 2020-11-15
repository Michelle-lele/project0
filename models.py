from sqlalchemy import Integer, Column, String
from sqlalchemy.types import Date, DateTime
from sqlalchemy_utils import force_auto_coercion, EmailType, UUIDType
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

'''
class Template(Base):
	__tablename__ = 'tepmlates'

	id = Column(Integer, primary_key= True, index=True)
	template_name = Column(String(30), nullable=False)
	template_path = 

class CV(Base):
	__tablename__ = "cvs"

	id = Column(UUIDType(binary=False), primary_key=True)
	user_id = 
	template_id = 
	names = 
	phone = 
	email = 
	website =
	summary = 


class Job(Base):
	__tablename__ = "jobs"

	id = Column(Integer, primary_key= True, index=True)
	user_id = 
	job_position = 
	organization = 
	job_location = 
	start_date = 
	end_date = 
	job_description = 

class Education(Base):
	__tablename__ = "education"

	id = Column(Integer, primary_key= True, index=True)
	user_id = 
	subject = 
	school = 
	start_date = 
	end_date = 
	description = 

class Skill(Base):
	__tablename__ = "skills"

	id = Column(Integer, primary_key= True, index=True)
	user_id = 
	skill_group = 
	skill = 

class Language(Base):
	__tablename__ = "languages"

	id = Column(Integer, primary_key= True, index=True)
	user_id = 
	language = 

class Project(Base):
	__tablename__ = "projects"

	id = Column(Integer, primary_key= True, index=True)
	user_id = 
	project_title = 
	project_url = 
	project_description = 
'''

Base.metadata.create_all(engine)