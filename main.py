from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from databaseAPI import base, engine

from routes.students import router
from routes.Course import router as course_router
from routes.Teacher import router as teacher_router
from routes.Enrollment import router as enrollment_router
from routes.Grade import router as grade_router


from models.Course import Course
from models.Teacher import teacherDB
from models.students import studentDB
from models.Enrollment import EnrollmentDB
from models.Grade import gradeDB

app = FastAPI(title = "university management system")
base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"message": "Welcome to the University Management System API!"}

app.include_router(router)
app.include_router(course_router)
app.include_router(teacher_router)
app.include_router(enrollment_router)
app.include_router(grade_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)