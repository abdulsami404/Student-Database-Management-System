import { useState, useEffect } from 'react'
import api from "./api/axios"

export default function Grades() {

    const [grades, setGrades] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [showForm, setShowForm] = useState(false)
    const [students, setStudents] = useState([])
    const [courses, setCourses] = useState([])
    const [newGrade, setNewGrade] = useState({
        studentID: "",
        courseID: "",
        grade: ""
    })

    useEffect(() => {
        api.get("/grades")
            .then(response => {
                setGrades(response.data)
                setLoading(false)
            })
            .catch(error => {
                console.log(error)
                setError("Failed to load grades")
                setLoading(false)
            })
    }, [])

    useEffect(() => {
        api.get("/students")
            .then(response => setStudents(response.data))
            .catch(error => console.log(error))
    }, [])

    useEffect(() => {
        api.get("/courses")
            .then(response => setCourses(response.data))
            .catch(error => console.log(error))
    }, [])

    function handleSave() {
        api.post("/grades/", newGrade)
            .then(response => {
                setGrades([...grades, response.data])
                setShowForm(false)
                setNewGrade({ studentID: "", courseID: "", grade: "" })
            })
            .catch(error => console.log(error))
    }

    function handleDelete(gradeID) {
        api.delete(`/grades/${gradeID}`)
            .then(() => {
                setGrades(grades.filter(g => g.gradeID !== gradeID))
            })
            .catch(error => console.log(error))
    }

    // helper to show names instead of IDs in the table
    function getStudentName(studentID) {
        const student = students.find(s => s.studentID === studentID)
        return student ? student.name : studentID
    }

    function getCourseName(courseID) {
        const course = courses.find(c => c.courseID === courseID)
        return course ? course.courseName : courseID
    }

    if (loading) return <p className="p-4">Loading...</p>
    if (error) return <p className="p-4 text-danger">{error}</p>

    return (
        <div className="container mt-4">

            <h2 className="mb-4">Grades</h2>

            <button
                className="btn btn-outline-success mb-3"
                onClick={() => setShowForm(!showForm)}
            >
                + ADD
            </button>

            {showForm && (
                <div className="card p-3 mb-4">
                    <h5>Add Grade</h5>

                    <select
                        className="form-select mb-2"
                        value={newGrade.studentID}
                        onChange={(e) => setNewGrade({ ...newGrade, studentID: e.target.value })}
                    >
                        <option value="">Select Student</option>
                        {students.map(student => (
                            <option key={student.studentID} value={student.studentID}>
                                {student.name}
                            </option>
                        ))}
                    </select>

                    <select
                        className="form-select mb-2"
                        value={newGrade.courseID}
                        onChange={(e) => setNewGrade({ ...newGrade, courseID: e.target.value })}
                    >
                        <option value="">Select Course</option>
                        {courses.map(course => (
                            <option key={course.courseID} value={course.courseID}>
                                {course.courseName}
                            </option>
                        ))}
                    </select>

                    <select
                        className="form-select mb-2"
                        value={newGrade.grade}
                        onChange={(e) => setNewGrade({ ...newGrade, grade: e.target.value })}
                    >
                        <option value="">Select Grade</option>
                        {["A+", "A", "B+", "B", "C+", "C", "D", "F"].map(g => (
                            <option key={g} value={g}>{g}</option>
                        ))}
                    </select>

                    <div className="d-flex gap-2">
                        <button className="btn btn-primary" onClick={handleSave}>
                            Save
                        </button>
                        <button className="btn btn-secondary" onClick={() => setShowForm(false)}>
                            Cancel
                        </button>
                    </div>
                </div>
            )}

            <table className="table table-striped table-hover">
                <thead className="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Student</th>
                        <th>Course</th>
                        <th>Grade</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {grades.map(grade => (
                        <tr key={grade.gradeID}>
                            <td>{grade.gradeID}</td>
                            <td>{getStudentName(grade.studentID)}</td>
                            <td>{getCourseName(grade.courseID)}</td>
                            <td>{grade.grade}</td>
                            <td>
                                <button
                                    className="btn btn-danger btn-sm"
                                    onClick={() => handleDelete(grade.gradeID)}
                                >
                                    DELETE
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

        </div>
    )
}