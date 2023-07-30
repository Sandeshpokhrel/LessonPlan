import React from "react";
import { Header } from "../Header/Header";

import Subject from "./Subjects/Subject";
export const Profile = () => {
  return (
    <>
      <Header />
      <div className="grid justify-center px-40">
        <div className="flex justify-center flex-wrap my-4 gap-16 px ">
          {/*starts the subject loop */}
          <Subject />
        </div>

        <div className="my-4">
          <input
            className="border-2 border-slate-500 mr-3 rounded p-1 "
            placeholder="Add Subject"
          />
          <button
            type="submit"
            className="button rounded bg-blue-500 py-1 px-2"
          >
            Create
          </button>
        </div>
      </div>
    </>
  );
};
