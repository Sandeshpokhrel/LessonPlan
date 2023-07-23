import React, { useState, useEffect } from "react";
import {useNavigate} from "react-router-dom";
import './login.css';
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
        <div className = "shadow-2xl mx-96 my-6">
            <form onSubmit={handleSubmit}>

                <div class="grid gap-5 place-content-center ">
                    
                    <div>
                        <h1 className="text-2xl flex justify-center my-4">Login</h1>
                    </div>
                    <div className="grid grid-cols-1">
                        <label for="username" className="">Username: </label>
                        <input id = "email" value = {email} type = "email" onChange = {handleText} className="email border-2 border-slate-400 rounded p-1" placeholder="Username/Email" required/>
                    </div>
                    
                    <div className="grid grid-cols-1">
                        <label for="password" className ="">Password: </label>
                        <input id = "password" value = {password} type = "password" onChange = {handlePass} className="password border-2 border-slate-400 rounded p-1" placeholder="Passcode" required/>
                    </div>
                    <div>
                        <input type = "submit" className="button rounded bg-blue-500 px-6 py-2" value = "login"/>
                    </div>
                    
                    <button onClick = {()=>navigate("/Register")} className= "linkbtn my-6">Don't have an account. <span>Register here.</span></button>
                </div>
            </form>
        </div>

        </>



    );
}
export default Login;