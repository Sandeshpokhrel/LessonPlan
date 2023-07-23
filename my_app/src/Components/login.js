import React, { useState, useEffect } from "react";
import {useNavigate} from "react-router-dom";
     const Login = ()=>{
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const handleText =(e) =>{ setEmail(e.target.value); }
    const handlePass = (e) =>{ setPassword(e.target.value); }
    let navigate =useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log('submitted');
        fetch('http://localhost:8000/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body:JSON.stringify({email:email, password:password})}
        )
        
        .then((response)=>{
            if(response.status === 200){
                navigate('/profile');
            }
            else if(response.status === 404 || response.status === 401){
                navigate('/');
                alert("Please enter valid username or Password!");                
            }
            return response.json();
        }).then((data)=>{
            localStorage.setItem('access', data.token.access);
            localStorage.setItem('refresh', data.token.refresh);
            console.log(localStorage);
        }) 
          
        
    }
    return(
        <>
        <div className = "Container">
            <h1 className="header">Login</h1>
            <form onSubmit={handleSubmit}>
                <input id = "email" value = {email} type = "email" onChange = {handleText}className="email" placeholder="Username/Email" required/>
                <input id = "password" value = {password} type = "password" onChange = {handlePass} className="password" placeholder="Passcode" required/>
                <input type = "submit" className="button" value = "login"/>
            </form>
            <button onClick = {()=>navigate("/Register")} className= "linkbtn">Don't have an account. Register here.</button>
        </div>

        </>



    );
}
export default Login;