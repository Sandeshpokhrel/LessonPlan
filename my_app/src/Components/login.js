import React, { useState, useEffect, useRef } from "react";
import {useNavigate} from "react-router-dom";
import { Header } from "./Header/Header";
import { Profile } from "./Profile/Profile";
import './login.css';
import axios from "../api/axios/axios";
    const Login = ()=>{
    const errRef = useRef();
    const userRef = useRef();
    const [user, setUser] = useState('');
    const [password, setPassword] = useState('');
    const [success, setSuccess] = useState(false);
    const [errMsg, setErrMsg] = useState('');
    const handleText =(e) =>{ setUser(e.target.value); }
    const handlePass = (e) =>{ setPassword(e.target.value); }
    let navigate =useNavigate();

    useEffect(()=>{
    setErrMsg('');
    },[user, password]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log('submitted');
        setUser('');
        setPassword('');
        setSuccess(true);
        try{

        }
        catch(err){

        }
        
    }
    return(
        
        <>
        <Header/>
        {success ? <Profile /> : (
        <div className = "shadow-2xl mx-96 my-6">
            <form onSubmit={handleSubmit}>
            <p ref = {errRef} className = {errMsg ? "errmsg": "offscreen"} aria-live="assertive">{errMsg}</p>

                <div class="grid gap-5 place-content-center ">
                    
                    <div>
                        <h1 className="text-2xl flex justify-center my-4">Login</h1>
                    </div>
                    <div className="grid grid-cols-1">
                        <label htmlFor="username" className="">Username: </label>
                        <input id = "username" value = {user} type = "text" onChange = {handleText} className="email border-2 border-slate-400 rounded p-1" placeholder="Username" autoComplete="off" required/>
                    </div>
                    
                    <div className="grid grid-cols-1">
                        <label htmlFor="password" className ="">Password: </label>
                        <input id = "password" value = {password} type = "password" onChange = {handlePass} className="password border-2 border-slate-400 rounded p-1" placeholder="Passcode" autoComplete="off" required/>
                    </div>
                    <div>
                        <input type = "submit" className="button rounded bg-blue-500 px-6 py-2" value = "login"/>
                    </div>
                    
                    <button onClick = {()=>navigate("/Register")} className= "linkbtn my-6">Don't have an account. <span>Register here.</span></button>
                </div>
            </form>
        </div>
        )}
        </>
        



    );
}
export default Login;