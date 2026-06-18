import React from 'react'
import { useState,useEffect } from 'react'
import api from './api/axios'
export default function Dashboard() {
  const [studentCount, setStudentCount] = useState(0)

  useEffect(() => {
    const fetchStudentCount = async () => {
      try {
        const response = await api.get('/students')
        setStudentCount(response.data.length)
      } catch (error) {
        console.error('Error fetching student count:', error)
      }
    }

    fetchStudentCount()
  }, [])

  return (
    <div>
      <div className="card" style={{ width: '18rem' }}>
  <div className="card-body">
    <h5 className="card-title">Number of Students</h5>
    <h6 className="card-subtitle mb-2 text-body-secondary">Card subtitle</h6>
    <p className="card-text">{studentCount} students enrolled</p>
    <a className="card-link">Card link</a>
    <a className="card-link">Another link</a>
  </div>
</div>
    </div>
  )
}
