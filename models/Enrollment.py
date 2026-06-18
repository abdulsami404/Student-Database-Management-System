from sqlalchemy import Column, Integer, String , ForeignKey 
from sqlalchemy.orm import relationship
from databaseAPI import base


class EnrollmentDB(base):
    __tablename__ = "enrollment"
    enrollmentID = Column(Integer, primary_key=True, index=True)
    studentID = Column(Integer, ForeignKey("students.studentID"))
    courseID = Column(Integer, ForeignKey("courses.courseID"))
    student = relationship("studentDB", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
