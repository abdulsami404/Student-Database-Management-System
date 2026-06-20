from pydantic import BaseModel

class GradeCreate(BaseModel):
    studentID: int
    courseID: int
    grade: str

class GradeResponse(BaseModel):
    gradeID: int
    studentID: int
    courseID: int
    grade : str

    class Config:
        from_attributes = True