import React, { useState, useEffect } from "react";
import {useNavigate} from "react-router-dom";

export const Header = () => {
  return (
    <>
    <div class="mx-20 mt-2">
      <div class="container">
        <div class="grid place-content-center bg-slate-500 p-5">
          <div>
            <div class="flex items-center">
              <img
                src="./icons/TUlogo.png"
                alt="Couldnot load image"
                class=""
              />
              <h1 class="text-3xl ml-4">Lesson Plan Management System</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
  </>
  )
}
