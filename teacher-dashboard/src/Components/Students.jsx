import { useEffect, useState } from "react"
import api from "./api/axios"
import "../index.css"

export default function Students() {

    const [students, setStudents] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [showForm, setShowForm] = useState(false)
    const [newStudent, setNewStudent] = useState({
        name: "",
        email: "",
        departmentID: "",
        semester: "",
        course: "",
        attendance: ""
    })
    const [courses, setCourses] = useState([])

    useEffect(() => {
        api.get("/students")
            .then(response => {
                setStudents(response.data)
                setLoading(false)
            })
            .catch(error => {
                console.log(error)
                setError("Failed to load students")
                setLoading(false)
            })
    }, [])

    useEffect(() => {
        api.get("/courses")
            .then(response => {
                setCourses(response.data)
            })
            .catch(error => {
                console.log(error)
            })
    }, [])

    function handleSave() {
        api.post("/students", newStudent)
            .then(response => {
                setStudents([...students, response.data])
                setShowForm(false)
                setNewStudent({
                    name: "",
                    email: "",
                    departmentID: "",
                    semester: "",
                    course: "",
                    attendance: ""
                })
            })
            .catch(error => {
                console.log(error)
            })
    }

    function handleDelete(studentID) {
        api.delete(`/students/${studentID}`)
            .then(() => {
                setStudents(students.filter(s => s.studentID !== studentID))
            })
            .catch(error => {
                console.log(error)
            })
    }

    if (loading) return <p className="p-4">Loading...</p>
    if (error) return <p className="p-4 text-danger">{error}</p>

    return (
        <div className="container mt-4">

            <h2 className="mb-4">Students</h2>

            <button
                type="button"
                className="btn btn-outline-success mb-3"
                onClick={() => setShowForm(!showForm)}
            >
                + ADD
            </button>

            {showForm && (
                <div className="card mt-3 p-3 mb-4">

                    <h4>Add Student</h4>

                    <input
                        className="form-control mb-2"
                        placeholder="Name"
                        value={newStudent.name}
                        onChange={(e) => setNewStudent({ ...newStudent, name: e.target.value })}
                    />
                    <input
                        className="form-control mb-2"
                        placeholder="Email"
                        value={newStudent.email}
                        onChange={(e) => setNewStudent({ ...newStudent, email: e.target.value })}
                    />
                    <input
                        className="form-control mb-2"
                        placeholder="Department ID"
                        value={newStudent.departmentID}
                        onChange={(e) => setNewStudent({ ...newStudent, departmentID: e.target.value })}
                    />
                    <input
                        className="form-control mb-2"
                        placeholder="Semester"
                        value={newStudent.semester}
                        onChange={(e) => setNewStudent({ ...newStudent, semester: e.target.value })}
                    />
                    <input
                        className="form-control mb-2"
                        placeholder="Attendance"
                        value={newStudent.attendance}
                        onChange={(e) => setNewStudent({ ...newStudent, attendance: e.target.value })}
                    />

                    <select
                        className="form-select mb-2"
                        value={newStudent.course}
                        onChange={(e) => setNewStudent({ ...newStudent, course: e.target.value })}
                    >
                        <option value="">Select Course</option>
                        {courses.map(course => (
                            <option key={course.courseID} value={course.courseID}>
                                {course.courseName}
                            </option>
                        ))}
                    </select>

                    <div className="d-flex gap-2">
                        <button className="btn btn-primary" onClick={handleSave}>
                            Save Student
                        </button>
                        <button className="btn btn-secondary" onClick={() => setShowForm(false)}>
                            Cancel
                        </button>
                    </div>

                </div>
            )}

            <div className="row g-3">
                {students.map(student => (
                    <div className="col-sm-6 col-lg-4" key={student.studentID}>
                        <div className="card h-100 shadow-sm">

                            <div className="card-header bg-dark text-white">
                                <div className="d-flex justify-content-between align-items-center">
                                    <h5 className="mb-0">{student.name}</h5>
                                    <button
                                        className="btn btn-danger btn-sm"
                                        onClick={() => handleDelete(student.studentID)}
                                    >
                                        DELETE
                                    </button>
                                </div>
                                <small>ID: {student.studentID}</small>
                            </div>

                            <div className="card-body">
                                <p className="mb-1"><strong>Course ID:</strong> {student.course}</p>
                                <p className="mb-1"><strong>Email:</strong> {student.email}</p>
                                <p className="mb-1"><strong>Department ID:</strong> {student.departmentID}</p>
                                <p className="mb-1"><strong>Semester:</strong> {student.semester}</p>
                            </div>

                            <div className="card-footer d-flex justify-content-between align-items-center">
                                <span className="text-muted">Attendance</span>
                                <span className={`badge ${student.attendance >= 75 ? "bg-success" : "bg-danger"}`}>
                                    {student.attendance}%
                                </span>
                            </div>

                        </div>
                    </div>
                ))}
            </div>

        </div>
    )
}