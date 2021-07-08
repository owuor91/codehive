from uuid import uuid4

from sqlalchemy import Column, String, Date, Enum
from sqlalchemy.dialects.postgresql import UUID

from app.base.model import Base
from app.enums import Nationality


class Student(Base):
    __tablename__ = "student"
    student_id = Column(
        UUID(as_uuid=True), nullable=False, default=uuid4, primary_key=True
    )
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone_number = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    nationality = Column(Enum(Nationality), nullable=False)
    password = Column(String(256), nullable=False)
