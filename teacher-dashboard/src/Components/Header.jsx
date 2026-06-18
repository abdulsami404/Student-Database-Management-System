import React from 'react'
import { Link } from "react-router-dom";
import  "../index.css"
export default function Header() {
  return (
    <header>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">

          <Link className="navbar-brand" to="/">
            Teacher Dashboard
          </Link>

          <button 
            className="navbar-toggler" 
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>

          <div className="collapse navbar-collapse" id="navbarNav">
            <div className="navbar-nav ms-auto">
              <Link className="nav-link" to="/">Dashboard</Link>
              <Link className="nav-link" to="/students">Students</Link>
              <Link className="nav-link" to="/courses">Courses</Link>
              <Link className="nav-link" to="/grades">Grades</Link>
            </div>
          </div>

        </div>
      </nav>
    </header>
  )
}