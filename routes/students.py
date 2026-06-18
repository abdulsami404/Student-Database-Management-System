from models.students import studentDB
from schemas.students import studentCreate,studentResponse
from fastapi import FastAPI,HTTPException,Depends,APIRouter

from databaseAPI import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/{student_id}", response_model=studentResponse)
def get_student(student_id:int,db:Session=Depends(get_db)):
    student = db.query(studentDB).filter(studentDB.studentID == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/",response_model=studentResponse)
def create_student(student:studentCreate,db:Session = Depends(get_db)):
    if db.query(studentDB).filter(studentDB.email == student.email).first():
        raise HTTPException(status_code=400, detail="Student with this email already exists")
    new_student = studentDB(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.put("/{student_id}",response_model=studentResponse)
def update_student(student_id:int,student:studentCreate,db:Session = Depends(get_db)):
    db_student = db.query(studentDB).filter(studentDB.studentID == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db_student.email = student.email
    db_student.departmentID = student.departmentID
    db_student.semester = student.semester
    db_student.course = student.course
    db_student.attendance = student.attendance
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/{student_id}")
def delete_student(student_id:int,db:Session = Depends(get_db)):
    student = db.query(studentDB).filter(studentDB.studentID == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}



