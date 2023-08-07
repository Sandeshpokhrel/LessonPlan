import React from 'react'
import useAxiosPrivate from '../../../packages/Auth/useAxiosPrivate'
import API_EP from '../../../utils/ApiEndPoint';
import { useEffect, useState } from 'react';
const SyllabusTile = (props) => {
    const axiosPrivate = useAxiosPrivate();
    const [syllabus, setSyllabus] = useState();
    const [bool, setBool] = useState(false);
    useEffect(()=>{
        let isMounted = true;
        const controller = new AbortController();
        const getSyllabus = async () =>{
            try{    
                const res = await axiosPrivate.get(`${API_EP.SECTIONS}${props.id}/chapters/`,{ signal: controller.signal});
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
    useEffect(()=>{
        let isMounted = true;
        const controller = new AbortController();
        const getSyllabus = async () =>{
            try{    
                const res = await axiosPrivate.get(`${API_EP.SECTIONS}${props.id}/chapters/`,{ signal: controller.signal});
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
    },[bool]);
    const handleDelete = async(e,id)=>{
            setBool(false);
            try{
                const res = await axiosPrivate.delete(API_EP.CHAPTER + `${id}/`)
                setBool(true);
            }catch(err){
              console.error(err);
            }
          }
    
  return (
    syllabus ? (
        syllabus.map((item)=>(
            <div class="px-32 pt-8">
            <div class="grid px-10 py-2 border-2 border-slate-500 rounded text-xl">
            <div>
          <button class="border-2 border-blue-400 bg-blue-400 rounded p-1 text-sm" onClick={(e)=>handleDelete(e,item.id)}>
            Delete entry 
        </button>
        </div>
              <div class="grid grid-cols-3 px-10 py-4">
            
                <div>
                  <ul class="list-none">
                    <li>{item.chapter_name}</li>
      
                    <div class="grid px-6 ul">
                    <ul class="list-disc">
                        {item.topic_set.map((nestitem)=>(
                            
                            <li>{nestitem.topic_name}</li>
                          
                        ))}
                    </ul>
                      
                    </div>
                  </ul>
                </div>
      
                
                <div>
                    {item.assignment_set.map((nesteditem)=>(
                        <div>
                        {nesteditem.assign_name}
                        <button class="border-2 border-blue-400 bg-blue-400 rounded p-1 text-sm">
                            Download
                        </button>
                    </div>
                    ))}
                  
                </div>
      
                
                <div>
                {item.resource_set.map((nesteditem)=>(
                            <div>
                            <button class="border-2 border-blue-400 bg-blue-400 rounded p-1 text-sm">
                                Download
                            </button>
                </div> 
                        ))}
                  
                </div>
              </div>
            </div>
          </div>
      )) 
      
    ) : ""
  
  )
}

export default SyllabusTile