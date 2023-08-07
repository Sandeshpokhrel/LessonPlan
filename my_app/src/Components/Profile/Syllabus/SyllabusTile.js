import React from 'react'
import useAxiosPrivate from '../../../packages/Auth/useAxiosPrivate'
import API_EP from '../../../utils/ApiEndPoint';
import { useEffect, useState } from 'react';
const SyllabusTile = () => {
    const axiosPrivate = useAxiosPrivate();
    const [syllabus, setSyllabus] = useState();
    useEffect(()=>{
        let isMounted = true;
        const controller = new AbortController();
        const getSyllabus = async () =>{
            try{    
                const res = await axiosPrivate.get(API_EP.SYLLABUS,{ signal: controller.signal});
                console.log(res.data);
                isMounted && setSyllabus(res.data);
            }catch(err){
                console.error(err);
            }
        }
        
        getSyllabus();
        return() => {
            isMounted = false;
            controller.abort();
        }
    },[]);
  return (
    syllabus ? (
        syllabus.map((item)=>(
            <div class="px-32 pt-8">
            <div class="grid px-10 py-2 border-2 border-slate-500 rounded text-xl">
              <div class="grid grid-cols-3 px-10 py-4">
            
                <div>
                  <ul class="list-none">
                    <li>2-D geometry</li>
      
                    <div class="grid px-6 ul">
                      <ul class="list-disc">
                          
                        <li>line</li>
                        <li>ellipse</li>
                        <li>circle</li>
                      </ul>
                    </div>
                  </ul>
                </div>
      
                
                <div>
                  <div>
                      2-d gemonetry assignment
                      <button class="border-2 border-blue-400 bg-blue-400 rounded p-1 text-sm">
                          Download
                      </button>
                  </div>
                </div>
      
                
                <div>
                  <div>
                      2-d gemonetry resources
                      <button class="border-2 border-blue-400 bg-blue-400 rounded p-1 text-sm">
                          Download
                      </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
      )) 
      
    ) : ""
  
  )
}

export default SyllabusTile