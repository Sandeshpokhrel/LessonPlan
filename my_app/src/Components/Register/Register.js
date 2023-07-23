import React, {useState} from "react";
import {useNavigate} from "react-router-dom";
export const Register = (props) =>{
    const [text, setText] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit =(e) =>{
        e.preventDefault();
    }
    let navigate = useNavigate();
    return (
        <>
        <div className="Container">
        <h1 className="header">Register</h1>
        <form onSubmit={handleSubmit}>
            <input value = {text} onChange = {(e)=>{setText(e.target.value);}}name = "FullName" type = "text" placeholder = "FullName"/>
            <input value = {email} onChange = {(e)=>{setEmail(e.target.value);}}name = "email" type = "email" placeholder = "Email"/>
            <input value = {email} onChange = {(e)=>{setEmail(e.target.value);}}name = "confirm_email" type = "email" placeholder = "Confirm Email"/>
            <input value = {password} onChange = {(e)=>{setPassword(e.target.value);}}name = "password" type = "password" placeholder = "password"/>
            <input value = {password} onChange = {(e)=>{setPassword(e.target.value);}}name = "confirm_password" type = "password" placeholder = "Confirm password"/>
            <input type = "submit" value = "Submit"/>        
        </form>
        <button onClick = {()=>navigate("/")} className="linkbtn">Already have an account? Login here.</button>
        </div>
        </>
    );
}