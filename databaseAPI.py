from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
import pymysql
import os
import dotenv

from pydantic import BaseModel
from typing import Optional

dotenv.load_dotenv()
app = FastAPI(title="student database management system")
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()

class studentDB(base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))
    age = Column(Integer)
    course = Column(String(50))
base.metadata.create_all(bind=engine)

class studentCreate(BaseModel):
    name: str
    email: str
    age: int
    course: str

class studentResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    course: str

    class Config:
        from_attributes = True

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Welcome to the student database management system!"}

@app.get("/students/{student_id}", response_model=studentResponse)
def get_student(student_id:int,db:Session=Depends(get_db)):
    student = db.query(studentDB).filter(studentDB.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students/",response_model=studentResponse)
def create_student(student:studentCreate,db:Session = Depends(get_db)):
    if db.query(studentDB).filter(studentDB.email == student.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    new_student = studentDB(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.put("/students/{student_id}",response_model=studentResponse)
def update_student(student_id:int,student:studentCreate,db:Session = Depends(get_db)):
    db_student = db.query(studentDB).filter(studentDB.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db_student.email = student.email
    db_student.age = student.age
    db_student.course = student.course
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete("/students/{student_id}")
def delete_student(student_id:int,db:Session = Depends(get_db)):
    student = db.query(studentDB).filter(studentDB.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}