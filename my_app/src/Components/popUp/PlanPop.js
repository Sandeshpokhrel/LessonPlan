import React from 'react'
import Button from "react-bootstrap/Button";
import { useState } from 'react';
import Modal from "react-bootstrap/Modal";
const PlanPop = () => {
    const [show, setShow] = useState(false);
  return (
    <>
    <Button variant="primary" onClick={() => setShow(true)}>
    Add Plan
  </Button>
    <Modal
    show={show}
    onHide={() => setShow(false)}
    dialogClassName="custom-modal"
    aria-labelledby="example-custom-modal-styling-title"
  >
    <Modal.Header>
      <Modal.Title id="example-custom-modal-styling-title">
        Plan
      </Modal.Title>

      {/* <p className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">
        {errMsg}
      </p> */}
    </Modal.Header>
    <Modal.Body>
      


    <div class="p-6 space-y-6">
            <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400" />

            <div class="flex flex-wrap gap-x-5">
              {/* first column */}
              <div>
                <div class="flex">
                  <input
                    class="border-2 rounded w-40"
                    placeholder="Week or Date"
                    name="name"
                    type="text"
                    required=""
                  />
                  <button
                    data-modal-hide="large-modal"
                    type="button"
                    class="ml-2 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                    // onClick={handleTopics}
                  >
                    Add
                  </button>
                </div>
              </div>
              {/* first row ends here */}


              {/* second column */}
              <div>
                <div class="grid gap-y-2">
                  <div>
                    <select
                      class="px-6 py-2 rounded mr-2"
                      name="chapterId"
                      required=""
                    >
                      <option value="">Chapters</option>

                      <option value="">fdffffffffffdsfafsafasfddsafdasfads</option>

                      <option value="">cfdfdf</option>
                    </select>

                    <select
                      class="px-6 py-2 rounded mr-2"
                      name="chapterId"
                      required=""
                    >
                      <option value="">Topics</option>

                      <option value="">fdfdf</option>

                      <option value="">cfdfdf</option>
                    </select>

                    <button
                      data-modal-hide="large-modal"
                      type="button"
                      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                    //   onClick={handleTopics}
                    >
                      Add
                    </button>
                  </div>

                  <div>
                    <ul class="list-decimal">
                      {/* first row */}
                      <li>
                        Addition
                        <span class="mx-2 ">--</span>
                        <span class=""> 4-bit addition</span>
                      </li>
                      {/* first row ends here */}

                      {/* second row */}
                      <li>
                        Subtraction
                        <span class="mx-2 ">--</span>
                        <span class=""> 2-bit</span>
                      </li>
                      {/* second row ends here */}
                    </ul>
                  </div>
                </div>
              </div>
              {/* second row ends here */}


              {/* third column */}
              <div>
                <div class="grid gap-y-2">
                  <div>
                    <select
                      class="px-6 py-2 rounded mr-2"
                      name="chapterId"
                      required=""
                    >
                      <option value="">Chapters</option>

                      <option value="">fdfdf</option>

                      <option value="">cfdsdfsdsadfasdfasdffdsffdf</option>
                    </select>

                    <select
                      class="px-6 py-2 rounded mr-2"
                      name="chapterId"
                      required=""
                    >
                      <option value="">Assign</option>

                      <option value="">fdfdf</option>

                      <option value="">cfdfdf</option>
                    </select>

                    <button
                      data-modal-hide="large-modal"
                      type="button"
                      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                    //   onClick={handleTopics}
                    >
                      Add
                    </button>
                  </div>

                  <div>
                    <ul class="list-decimal">
                      {/* first row */}
                      <li>
                        Addition
                        <span class="mx-2 ">--</span>
                        <span class=""> 4-bit INSIDE SAMIP</span>
                      </li>
                      {/* first row ends here */}

                      {/* second row */}
                      <li>
                        Subtraction
                        <span class="mx-2 ">--</span>
                        <span class=""> GANDU CEO SAMIP </span>
                      </li>
                      {/* second row ends here */}
                    </ul>
                  </div>
                </div>
              </div>
              {/* third column ends here */}


              {/* fourth column */}
              <div>
                <div class="grid gap-y-2">
                  <div>
                    <select
                      class="px-6 py-2 rounded mr-2"
                      name="chapterId"
                      required=""
                    >
                      <option value="">Chapters</option>

                      <option value="">fdfdf</option>

                      <option value="">cfdfdf</option>
                    </select>

                    <select
                      class="px-6 py-2 rounded mr-2"
                      name="chapterId"
                      required=""
                    >
                      <option value="">Resources</option>

                      <option value="">fdfdf</option>

                      <option value="">cfdfdf</option>
                    </select>

                    <button
                      data-modal-hide="large-modal"
                      type="button"
                      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                    //   onClick={handleTopics}
                    >
                      Add
                    </button>
                  </div>

                  <div>
                    <ul class="list-decimal">
                      {/* first row */}
                      <li>
                        Addition
                        <span class="mx-2 ">--</span>
                        <span class=""> 4-bit resources</span>
                      </li>
                      {/* first row ends here */}

                      {/* second row */}
                      <li>
                        Subtraction
                        <span class="mx-2 ">--</span>
                        <span class=""> GANDU CEO resources </span>
                      </li>
                      {/* second row ends here */}
                    </ul>
                  </div>
                </div>
              </div>
              {/* fourth ends here */}
            </div>
          </div>


    </Modal.Body>
    <Modal.Footer>
          <Button variant="primary" >
            Save Changes
          </Button>
        </Modal.Footer>
  </Modal>
    </>
    
  )
}

export default PlanPop