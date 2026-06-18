from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from databaseAPI import base

class gradeDB(base):
    __tablename__ = "grades"
    gradeID = Column(Integer, primary_key=True, index=True)
    studentID = Column(Integer , ForeignKey("students.studentID"))
    courseID = Column(Integer , ForeignKey("courses.courseID"))
    grade = Column(String(2))
    student = relationship("studentDB", back_populates="grades")
    course = relationship("Course", back_populates="grades")