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
        <div className="shadow-2xl mx-96 my-6">
        <form onSubmit={handleSubmit}>
                <div class="grid gap-4 place-content-center ">
                    
                    <div>
                        <h1 className="text-2xl flex justify-center my-4">Register</h1>
                    </div>
                    <div className="grid grid-cols-2">
                        <label for="Fullname" className="">FullName: </label>

                        <input value = {text} className = "border-2 border-slate-400 rounded p-1 " onChange = {(e)=>{setText(e.target.value);}}name = "FullName" type = "text" placeholder = "FullName"/>

                    </div>
                    
                    <div className="grid grid-cols-2 ">
                        <label for="email" className ="">Email: </label>
                       <input value = {email} className = "border-2 border-slate-400 rounded p-1 " onChange = {(e)=>{setEmail(e.target.value);}}name = "email" type = "email" placeholder = "Email"/>

                    </div>
                    <div className="grid grid-cols-2 ">
                        <label for="confirm_email" className ="">Confirm Email : </label>
                         <input value = {email} className = "border-2 border-slate-400 rounded p-1 " onChange = {(e)=>{setEmail(e.target.value);}}name = "confirm_email" type = "email" placeholder = "Confirm Email"/>

                    </div>
                    <div className="grid grid-cols-2 ">
                        <label for="password" className ="">Password: </label>
                        <input value = {password} className = "border-2 border-slate-400 rounded p-1 " onChange = {(e)=>{setPassword(e.target.value);}}name = "password" type = "password" placeholder = "password"/>
                    </div>
                    <div className="grid grid-cols-2 ">
                        <label for="password" className ="">Confirm Password: </label>
                        <input value = {password} className = "border-2 border-slate-400 rounded p-1 " onChange = {(e)=>{setPassword(e.target.value);}}name = "confirm_password" type = "password" placeholder = "Confirm password"/>
                    </div>
                    

                    <div>
                        <input type = "submit" className = "border-2 border-slate-400 rounded p-1 " value = "Submit" className="button rounded bg-blue-500 px-6 py-2"/>        
                    </div>
                <button onClick = {()=>navigate("/")} className="linkbtn my-6">Already have an account? Login here.</button>
             </div>
            

        </form>
        </div>
        </>
    );
}