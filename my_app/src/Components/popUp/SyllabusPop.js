import React from 'react'
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import 'flowbite/dist/flowbite.min.css';
const SyllabusPop = () => {
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const handleConfirm = async(e) =>{
        
          handleClose();
          
    
     
      }
  return (
    <>
    <button onClick = {handleShow} type="submit" className="button rounded bg-blue-500 p-1" >
              Add Syllabus
        </button>
    <Modal
    show={show}
    onHide={handleClose}
    backdrop="static"
    keyboard={false}
  >
    <Modal.Header closeButton>
      <Modal.Title>Add department/Section Name</Modal.Title>
    </Modal.Header>
    <Modal.Body>
    <div class="p-6 space-y-6">
    <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400"/>

    <div class="grid grid-cols-3 ">
        <div >
            <div>
                <input type="text" placeholder="Chapters" width="10px" class="border-2 rounded p-1 border-slate-500"/>
                <button data-modal-hide="large-modal" type="button" 
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Add
                </button>
            </div>

            <div class="ml-6 my-2">
                <input type="text" placeholder="Topics" class="border-2 rounded p-1 border-slate-500" />
                <button data-modal-hide="large-modal" type="button" 
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Add
                </button>
            </div>



        </div>

        <div>
            <div>
                <input type="text" placeholder="Assignment" class="border-2 rounded p-1 border-slate-500" />
                
                <form action="/action_page.php" class="my-2">
                    <input type="file" id="myFile" name="filename" placeholder="upload"/>
                </form>

            </div>

            <div class="relative h-32 w-60">
                    <button data-modal-hide="large-modal" type="button" 
                    class=" text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Add
                    </button>
              </div>

        </div>

        <div>
            <div>
                <input type="text" placeholder="Resources" class="border-2 rounded p-1 border-slate-500" />
                <button data-modal-hide="large-modal" type="button" 
                class=" text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Add
                </button>
            </div>



        </div>


    </div>


            
            <div class="flex items-center p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600 ">
                <button data-modal-hide="extralarge-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Upload</button>
                <button data-modal-hide="extralarge-modal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Cancel</button>
            </div>
        </div>
    
    </Modal.Body>
    <Modal.Footer>
      <Button variant="secondary" onClick={handleClose}>
        Close
      </Button>
      <Button variant="primary" onClick = {handleConfirm}>Confirm</Button>
    </Modal.Footer>
  </Modal>
    </>
    

    
  )
}

export default SyllabusPop