import React from 'react'
import { Header } from '../../Header/Header'
import NavBar from '../../NavBar/NavBar'
import { useLocation } from 'react-router-dom'
import PlanPop from '../../popUp/PlanPop'
const Plan = () => {
    const location = useLocation();
    const section = location.state?.section;
    const id = location.state?.id;
  return (
    <>
    <Header />
    <NavBar section = {section} page = {true}/>
    <PlanPop/>
    
    </>
  )
}

export default Plan