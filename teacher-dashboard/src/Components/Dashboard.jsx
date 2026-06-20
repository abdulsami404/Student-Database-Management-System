import { useState, useEffect } from 'react'
import api from './api/axios'

export default function Dashboard() {

  const [studentCount, setStudentCount] = useState(0)
  const [courseCount, setCourseCount] = useState(0)
  const [gradeCount, setGradeCount] = useState(0)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([
      api.get('/students'),
      api.get('/courses'),
      api.get('/grades')
    ])
      .then(([students, courses, grades]) => {
        setStudentCount(students.data.length)
        setCourseCount(courses.data.length)
        setGradeCount(grades.data.length)
        setLoading(false)
      })
      .catch(error => {
        console.error(error)
        setLoading(false)
      })
  }, [])

  if (loading) return <p className="p-4">Loading...</p>

  const stats = [
    { label: "Total Students", value: studentCount, color: "primary" },
    { label: "Total Courses",  value: courseCount, color: "success" },
    { label: "Grades Recorded", value: gradeCount, color: "warning" },
  ]

  return (
    <div className="container mt-4">

      <h2 className="mb-1">Dashboard</h2>
      <p className="text-muted mb-4">Welcome back, Teacher</p>

      <div className="row g-3">
        {stats.map(stat => (
          <div className="col-sm-6 col-lg-4" key={stat.label}>
            <div className={`card border-${stat.color} shadow-sm h-100`}>
              <div className="card-body d-flex align-items-center gap-3">
                <span style={{ fontSize: "2.5rem" }}>{stat.icon}</span>
                <div>
                  <h6 className="text-muted mb-0">{stat.label}</h6>
                  <h2 className="mb-0">{stat.value}</h2>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

    </div>
  )
}