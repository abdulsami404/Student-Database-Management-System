from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from databaseAPI import base

class Course(base):
    __tablename__ = "courses"
    courseID = Column(Integer, primary_key=True, index=True)
    courseName = Column(String(50) , nullable = False)
    creditHours = Column(Integer , nullable = False)
    teacherID = Column(Integer , ForeignKey("teachers.teacherID"))
    teachers = relationship("teacherDB", back_populates="courses")
    enrollments = relationship("EnrollmentDB", back_populates="course")
    grades = relationship("gradeDB", back_populates="course")