
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from databaseAPI import base

class studentDB(base):
    __tablename__ = "students"
    studentID = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    course = Column(String(50))
    departmentID = Column(Integer)
    semester = Column(Integer)
    attendance = Column(Integer)
    enrollments = relationship("EnrollmentDB", back_populates="student")
    grades = relationship("gradeDB", back_populates="student")