from pydantic import BaseModel

class TeacherCreate(BaseModel):
    name: str
    email: str
    departmentID: int

class TeacherResponse(BaseModel):
    teacherID: int
    name: str
    email: str
    departmentID: int

    class Config:
        from_attributes = True
