import React from 'react'
import useAuth from './useAuth'
import axios from '../../api/axios/axios';
export const UseRefreshToken = () => {
  const {setAuth} = useAuth();
  const refresh = async () =>{
    const res = await axios.get('/auth/jwt/refresh',{
      withCredentials: true
    });
    setAuth(prev =>{
      console.log(JSON.stringify(prev));
      console.log(res.data.access);
      return{...prev, accessToken: res.data.access};
    })
    return res.data.access;
  }

  return (
    refresh
  );
}
