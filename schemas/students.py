
from pydantic import BaseModel


class studentCreate(BaseModel):
    name: str
    email: str
    departmentID: int
    semester: int
    course: str
    attendance: int

class studentResponse(BaseModel):
    studentID: int
    name: str
    course: str
    email: str
    departmentID: int
    semester: int
    attendance: int

    class Config:
        from_attributes = True


        
# class studentDB(base):
#     __tablename__ = "students"
#     studentID = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50))
#     email = Column(String(50), unique=True)
#     course = Column(String(50))
#     departmentID = Column(Integer)
#     semester = Column(Integer)
#     attendance = Column(Integer)