
from schemas.Enrollment import EnrollmentCreate,EnrollmentResponse
from models.students import studentDB
from models.Course import Course
from models.Enrollment import EnrollmentDB
from fastapi import HTTPException,Depends,APIRouter

from databaseAPI import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.get("/{enrollment_id}", response_model=EnrollmentResponse)
def get_enrollment(enrollment_id:int,db:Session = Depends(get_db)):
    enrollment = db.query(EnrollmentDB).filter(EnrollmentDB.enrollmentID == enrollment_id).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@router.post("/",response_model=EnrollmentResponse)
def create_enrollment(enrollment:EnrollmentCreate,db:Session = Depends(get_db)):
    student = db.query(studentDB).filter(studentDB.studentID == enrollment.studentID).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    course = db.query(Course).filter(Course.courseID == enrollment.courseID).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    existing = db.query(EnrollmentDB).filter(
    EnrollmentDB.studentID == enrollment.studentID,
    EnrollmentDB.courseID == enrollment.courseID
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")

    new_enrollment = EnrollmentDB(**enrollment.model_dump())
    try:
        db.add(new_enrollment)
        db.commit()
        db.refresh(new_enrollment)
    except Exception as e:
        db.rollback()
        print("Enrollment Error:", e)
        raise HTTPException(status_code=500, detail=str(e)) 
    return new_enrollment

@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id:int, db:Session = Depends(get_db)):
    enrollment = db.query(EnrollmentDB).filter(EnrollmentDB.enrollmentID == enrollment_id).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    try:
        db.delete(enrollment)
        db.commit()
    except Exception as e:
        db.rollback()
        print("Enrollment Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Enrollment deleted successfully"}