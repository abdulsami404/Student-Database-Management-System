from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from databaseAPI import base

class teacherDB(base):
    __tablename__ = "teachers"
    teacherID = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    departmentID = Column(Integer)
    courses = relationship("Course", back_populates="teachers")