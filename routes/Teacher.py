
from schemas.Teacher import TeacherCreate,TeacherResponse
from models.Teacher import teacherDB
from fastapi import HTTPException,Depends,APIRouter

from databaseAPI import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/teachers", tags=["Teachers"])

@router.get("/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id:int,db:Session = Depends(get_db)):
    teacher = db.query(teacherDB).filter(teacherDB.teacherID == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.post("/",response_model=TeacherResponse)
def create_teacher(teacher:TeacherCreate,db:Session = Depends(get_db)):
    if db.query(teacherDB).filter(teacherDB.email == teacher.email).first():
        raise HTTPException(status_code=400, detail="Teacher with this email already exists")
    new_teacher = teacherDB(**teacher.model_dump())
    try:   
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
    except Exception as e:
        db.rollback()
        raise 
    return new_teacher

@router.put("/{teacher_id}",response_model=TeacherResponse)
def update_teacher(teacher_id:int, teacher:TeacherCreate, db:Session = Depends(get_db)):
    db_teacher = db.query(teacherDB).filter(teacherDB.teacherID == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db_teacher.name = teacher.name
    db_teacher.email = teacher.email
    db_teacher.departmentID = teacher.departmentID
    try:
        db.commit()
        db.refresh(db_teacher)
    except Exception as e:
        db.rollback()
        raise 
    return db_teacher

@router.delete("/{teacher_id}")
def delete_teacher(teacher_id:int, db:Session = Depends(get_db)):
    teacher = db.query(teacherDB).filter(teacherDB.teacherID == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete(teacher)
    db.commit()
    return {"message": "Teacher deleted successfully"}