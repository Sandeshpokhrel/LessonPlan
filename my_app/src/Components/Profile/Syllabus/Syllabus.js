import React from 'react'
import { Header } from '../../Header/Header';
import NavBar from '../../NavBar/NavBar';
import SyllabusPop from '../../popUp/SyllabusPop';
import { useLocation } from 'react-router-dom';
const Syllabus = () => {
  const location = useLocation();
  const section = location.state?.section;
  const id = location.state?.id;
  return (
    <>
    <Header />
    <NavBar page = {true} section = {section}/>
      <SyllabusPop id = {id}/>
    
    </>
    
  )
}

export default Syllabus;
