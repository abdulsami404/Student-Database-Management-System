import {Routes, Route} from "react-router-dom"
import Header  from "./Components/Header"

import Dashboard from "./Components/Dashboard"
import Students from "./Components/Students"
import Courses from "./Components/Courses"
import Grades from "./Components/Grades"
function App() {
  return(
    <>
      <Header/>
      <Routes>
        <Route path="/" element={<Dashboard/>}/>
        <Route path="/students" element={<Students/>}/>
        <Route path="/courses" element={<Courses/>}/>
        <Route path="/grades" element={<Grades/>}/>
      </Routes>
    </>
  );

  
}

export default App
