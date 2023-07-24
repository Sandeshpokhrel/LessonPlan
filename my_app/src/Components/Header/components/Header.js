import React, { useState, useEffect } from "react";
import {useNavigate} from "react-router-dom";

export const Header = () => {
  return (
    <>
    <div class="flex items-center">
      <img
        src="./icons/TUlogo.png"
        alt="Couldnot load image"
        class=""
      />
      <h1 class="text-3xl ml-4">Lesson Plan Management System</h1>
    </div>
  </>
  )
}
