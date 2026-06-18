from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    studentID: int
    courseID: int

class EnrollmentResponse(BaseModel):
    enrollmentID: int
    studentID: int
    courseID: int
    
    class Config:
        from_attributes = True