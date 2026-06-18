from models.Course import Course
from models.Teacher import teacherDB
from schemas.Course import CourseCreate,CourseResponse
from fastapi import HTTPException,Depends,APIRouter

from databaseAPI import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id:int,db:Session = Depends(get_db)):
    course = db.query(Course).filter(Course.courseID == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.post("/",response_model=CourseResponse)
def create_course(course:CourseCreate,db:Session = Depends(get_db)):
    teacher = db.query(teacherDB).filter(
        teacherDB.teacherID == course.teacherID
    ).first()

    if not teacher:
        raise HTTPException(
        status_code=404,
        detail="Teacher not found"
        )
    new_course = Course(**course.model_dump())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@router.put("/{course_id}",response_model=CourseResponse)
def update_course(course_id:int, course:CourseCreate, db:Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.courseID == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db_course.courseName = course.courseName
    db_course.creditHours = course.creditHours
    teacher = db.query(teacherDB).filter(
        teacherDB.teacherID == course.teacherID
    ).first()

    if not teacher:
        raise HTTPException(
        status_code=404,
        detail="Teacher not found"
        )
    db.commit()
    db.refresh(db_course)
    return db_course

@router.delete("/{course_id}")
def delete_course(course_id:int, db:Session = Depends(get_db)):
    course = db.query(Course).filter(Course.courseID == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return {"message": "Course deleted successfully"}

