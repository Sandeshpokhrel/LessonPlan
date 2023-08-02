import API_EP from "../../../utils/ApiEndPoint";
import Edit from "../components/edit.png";
import Delete from "../components/del.png";
import { useEffect, useState } from "react";
import useAxiosPrivate from '../../../packages/Auth/useAxiosPrivate'
const Subject = () => {
    const [subject, setSubject] = useState();
    const axiosPrivate = useAxiosPrivate();
    useEffect(()=>{
        let isMounted = true;
        const controller = new AbortController();
        const getSubjects = async () =>{
            try{    
                const res = await axiosPrivate.get(API_EP.SUBJECTS,{ signal: controller.signal});
                console.log(res.data);
                isMounted && setSubject(res.data);
            }catch(err){
                console.error(err);
            }
        }
        getSubjects();
        return() => {
            isMounted = false;
            controller.abort();
        }
    },[])
  return (
    <div className="border-solid border-2 border-slate-500 rounded px-10 py-6 grid gap-y-4 hover:scale-105 ">
            <div className="border-solid border-1 border-blue-500  text-2xl grid justify-center mb-4">
              COA
            </div>
            {/*starts Department loop */}
            <div className="grid grid-cols-3">
              <span>BCT</span>
              <button type="submit" className="p-1 mx-1">
                <img src={Edit} className="h-4 w-4" alt="" />
              </button>
              <button type="submit" className="p-1">
                <img
                  src={Delete}
                  className="h-4 w-4"
                  alt="couldnot show icon"
                />
              </button>
            </div>
            {/*starts another department loop 2 */}
            <div className="grid grid-cols-3">
              <span>BEI</span>
              <button type="submit" className="p-1 mx-1">
                <img src={Edit} className="h-4 w-4" alt="" />
              </button>
              <button type="submit" className="p-1">
                <img
                  src={Delete}
                  className="h-4 w-4"
                  alt="couldnot show icon"
                />
              </button>
            </div>

            <button type="submit" className="button rounded bg-blue-500 p-1">
              Add
            </button>
            <div className="grid grid-cols-2 gap-x-2">
              <button type="submit" className="button rounded bg-blue-500 p-1">
                Edit
              </button>
              <button type="submit" className="button rounded bg-blue-500 p-1">
                Delete
              </button>
            </div>
          </div>
  )
}
export default Subject;
