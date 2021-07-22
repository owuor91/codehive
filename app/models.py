from uuid import uuid4

from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID,ENUM

from app.base.model import Base
from app.enums import Nationality


class Student(Base):
    __tablename__ = "student"
    student_id = Column(
        UUID(as_uuid=True), nullable=False, default=uuid4, primary_key=True
    )
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(50), nullable=False, unique=True)
    date_of_birth = Column(Date, nullable=False)
    nationality = Column(ENUM(Nationality), nullable=False)
    password = Column(String(256), nullable=False)


class Course(Base):
    __tablename__ = "course"
    course_id = Column(UUID(as_uuid=True), nullable=False, default=uuid4,
                       primary_key=True)
    course_name = Column(String(100), nullable=False, unique=True)
    course_code = Column(String(100), nullable=False)
    description = Column(String(250),nullable=False)
    instructor = Column(String(100), nullable=False)