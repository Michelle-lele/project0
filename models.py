from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date, DateTime
from sqlalchemy_utils import force_auto_coercion, EmailType, UUIDType
from database import Base, engine, db
import datetime

#Base.metadata.clear()
force_auto_coercion()

class User(Base):
	__tablename__ = 'users'

	user_id = Column(Integer, primary_key=True, index=True)
	username = Column(String(30), nullable=False)
	email = Column(EmailType(length=255), unique=True, nullable=False)
	password = Column(String(200), nullable=False)
	registered_at = Column(DateTime, default=datetime.datetime.utcnow)
	CVs = relationship("CV")
	jobs = relationship("Job")
	education = relationship("Education")
	skills = relationship("Skill")
	languages = relationship("Language")
	projects = relationship("Project")

class Template(Base):
	__tablename__ = 'templates'

	template_id = Column(Integer, primary_key= True, index=True)
	template_name = Column(String(30), unique=True, nullable=False)
	template_path = Column(String(), nullable=False)
	CVs = relationship("CV")


class CV(Base):
	__tablename__ = "cvs"

	cv_id = Column(UUIDType(binary=False), primary_key=True)
	user_id = Column(Integer, ForeignKey('users.user_id'))
	template_id = Column(Integer, ForeignKey('templates.template_id'))
	names = Column(String(30))
	phone = Column(String(20))
	email = Column(String(50))
	website = Column(String(50))
	summary = Column(String(250))

class Job(Base):
	__tablename__ = "jobs"

	job_id = Column(Integer, primary_key= True, index=True)
	user_id = Column(Integer, ForeignKey('users.user_id'))
	job_position = Column(String(30), nullable=False)
	organization = Column(String(60), nullable=False)
	job_location = Column(String(50))
	start_date = Column(Date, nullable=False)
	end_date = Column(Date, nullable=False)
	job_description = Column(String(250))

class Education(Base):
	__tablename__ = "education"

	education_id = Column(Integer, primary_key= True, index=True)
	user_id = Column(Integer, ForeignKey('users.user_id'))
	subject = Column(String(30), nullable=False)
	school = Column(String(30), nullable=False)
	start_date = Column(Date, nullable=False)
	end_date = Column(Date, nullable=False)
	description = Column(String(80), nullable=False)

class Skill(Base):
	__tablename__ = "skills"
	skill_id = Column(Integer, primary_key= True, index=True)
	user_id = Column(Integer, ForeignKey('users.user_id'))
	#skill_group = Column(String(30), nullable=False, default="Default")
	skill = Column(String(30), nullable=False)


class Language(Base):
	__tablename__ = "languages"

	language_id = Column(Integer, primary_key= True, index=True)
	user_id = Column(Integer, ForeignKey('users.user_id'))
	language = Column(String(20), nullable=False, default="English")

class Project(Base):
	__tablename__ = "projects"

	project_id = Column(Integer, primary_key= True, index=True)
	user_id = Column(Integer, ForeignKey('users.user_id'))
	project_title = Column(String(60), nullable=False)
	project_url = Column(String(200))
	project_description = Column(String(250))

Base.metadata.create_all(engine)