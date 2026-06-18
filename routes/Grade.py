from schemas.Grade import GradeCreate,GradeResponse
from models.Grade import gradeDB
from models.students import studentDB
from models.Course import Course

from fastapi import HTTPException,Depends,APIRouter

from databaseAPI import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/grades", tags=["Grades"])

@router.get("/{grade_id}", response_model=GradeResponse)
def get_grade(grade_id:int,db:Session = Depends(get_db)):
    grade = db.query(gradeDB).filter(gradeDB.gradeID == grade_id).first()
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    return grade

@router.post("/",response_model=GradeResponse)
def create_grade(grade:GradeCreate,db:Session = Depends(get_db)):
    student = db.query(studentDB).filter(studentDB.studentID == grade.studentID).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    course = db.query(Course).filter(Course.courseID == grade.courseID).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    existing = db.query(gradeDB).filter(
    gradeDB.studentID == grade.studentID,
    gradeDB.courseID == grade.courseID
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Grade already exists for this student-course pair")
    new_grade = gradeDB(**grade.model_dump())
    try:
        db.add(new_grade)
        db.commit()
        db.refresh(new_grade)
    except Exception as e:
        db.rollback()
        print("Grade Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
    return new_grade

@router.delete("/{grade_id}")
def delete_grade(grade_id:int, db:Session = Depends(get_db)):
    grade = db.query(gradeDB).filter(gradeDB.gradeID == grade_id).first()
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    try:
        db.delete(grade)
        db.commit()
    except Exception as e:
        db.rollback()
        print("Grade Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Grade deleted successfully"}