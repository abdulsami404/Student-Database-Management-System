import { useState, useEffect } from 'react'
import api from "./api/axios"

export default function Courses() {

    const [courses, setCourses] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [showForm, setShowForm] = useState(false)
    const [newCourse, setNewCourse] = useState({
        courseName: "",
        creditHours: "",
        teacherID: ""
    })

    useEffect(() => {
        api.get("/courses")
            .then(response => {
                setCourses(response.data)
                setLoading(false)
            })
            .catch(error => {
                console.log(error)
                setError("Failed to load courses")
                setLoading(false)
            })
    }, [])

    function handleSave() {
        api.post("/courses/", newCourse)
            .then(response => {
                setCourses([...courses, response.data])
                setShowForm(false)
                setNewCourse({ courseName: "", creditHours: "", teacherID: "" })
            })
            .catch(error => console.log(error))
    }

    function handleDelete(courseID) {
        api.delete(`/courses/${courseID}`)
            .then(() => {
                setCourses(courses.filter(c => c.courseID !== courseID))
            })
            .catch(error => console.log(error))
    }

    if (loading) return <p className="p-4">Loading...</p>
    if (error) return <p className="p-4 text-danger">{error}</p>

    return (
        <div className="container mt-4">

            <h2 className="mb-4">Courses</h2>

            <button
                className="btn btn-outline-success mb-3"
                onClick={() => setShowForm(!showForm)}
            >
                + ADD
            </button>

            {showForm && (
                <div className="card p-3 mb-4">
                    <h5>Add Course</h5>

                    <input
                        className="form-control mb-2"
                        placeholder="Course Name"
                        value={newCourse.courseName}
                        onChange={(e) => setNewCourse({ ...newCourse, courseName: e.target.value })}
                    />
                    <input
                        className="form-control mb-2"
                        placeholder="Credit Hours"
                        type="number"
                        value={newCourse.creditHours}
                        onChange={(e) => setNewCourse({ ...newCourse, creditHours: e.target.value })}
                    />
                    <input
                        className="form-control mb-2"
                        placeholder="Teacher ID"
                        type="number"
                        value={newCourse.teacherID}
                        onChange={(e) => setNewCourse({ ...newCourse, teacherID: e.target.value })}
                    />

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
                        <th>Course Name</th>
                        <th>Credit Hours</th>
                        <th>Teacher ID</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {courses.map(course => (
                        <tr key={course.courseID}>
                            <td>{course.courseID}</td>
                            <td>{course.courseName}</td>
                            <td>{course.creditHours}</td>
                            <td>{course.teacherID}</td>
                            <td>
                                <button
                                    className="btn btn-danger btn-sm"
                                    onClick={() => handleDelete(course.courseID)}
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