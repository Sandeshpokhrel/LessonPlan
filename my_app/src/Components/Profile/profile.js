import React from 'react'

export const Profile = () => {
  return (
    <>
    <div className="grid justify-center px-40">

<div className="flex justify-center flex-wrap my-4 gap-16 px ">

    <div className="border-solid border-2 border-slate-500 rounded px-10 py-6 grid gap-y-4 hover:scale-105 ">
        <div className="border-solid border-1 border-blue-500  text-2xl grid justify-center mb-4">COA</div> 

        <div className="grid grid-cols-3">
            <span>BCT</span>
            <button type = "submit"  className="p-1 mx-1">< img src="/my_app/src/Components/Profile/components/edit.png" className="h-4 w-4" alt="" /></button>    
            <button type = "submit"  className="p-1"><img src="/my_app/src/Components/Profile/components/del.png"  className="h-4 w-4" alt="couldnot show icon" /></button>    
        </div>
        <div className="grid grid-cols-3">
            <span>BEI</span>
            <button type = "submit"  className="p-1 mx-1"><img src="/my_app/src/Components/Profile/components/edit.png" className="h-4 w-4" alt="" /></button>    
            <button type = "submit"  className="p-1"><img src="/my_app/src/Components/Profile/components/del.png"  className="h-4 w-4" alt="couldnot show icon" /></button>    

        </div>

        <button type = "submit"  className="button rounded bg-blue-500 p-1">Add</button>    
        <div className="grid grid-cols-2 gap-x-2">
            <button type = "submit"  className="button rounded bg-blue-500 p-1">Edit</button>    
            <button type = "submit"  className="button rounded bg-blue-500 p-1">Delete</button>    
        </div>

        
    </div>       
    
</div>

<div className="my-4">
    <input className="border-2 border-slate-500 rounded p-1 " placeholder="Add Subject" />
    <button type = "submit" className="button rounded bg-blue-500 py-1 px-2">Create</button>

</div>

</div>
  
    
</>
  )
}
