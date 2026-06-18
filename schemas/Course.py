from pydantic import BaseModel

class CourseCreate(BaseModel):
    courseName: str
    creditHours: int
    teacherID: int

class CourseResponse(BaseModel):
    courseID: int
    courseName: str
    creditHours: int
    teacherID: int

    class Config:
        from_attributes = True

            
# class courseDB(base):
#     __tablename__ = "courses"
#     courseID = Column(Integer, primary_key=True, index=True)
#     courseName = Column(String(50))
#     creditHours = Column(Integer)
#     teacherID = Column(Integer)