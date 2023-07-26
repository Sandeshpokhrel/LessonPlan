import logo from './logo.svg';
import './App.css';
import Login from './Components/login'
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import { Register } from './Components/Register/Register';
import { Profile } from './Components/Profile/Profile';
function App() {
  return (
    <Router>
        <Routes>
          {/* <Route element = {<PrivRoutes/>}> */}
          <Route element = {<Login/>} path = "/" exact/>
          <Route element = {<Profile/>} path = "/Profile" />
          {/* </Route> */}
           <Route element = {<Register/>} path = "/Register" /> 
        </Routes>
    </Router>
  );
}

export default App;
