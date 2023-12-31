import React from "react";
import { AiOutlineStar } from "react-icons/ai";
import { JobCard } from "../components/JobCard";
import { Accordion } from "../components/Accordion";

const Dashboard = () => {
  return (
    <div className="grid grid-cols-12 space-y-5 md:space-y-0 md:space-x-5">
      <div className="col-span-12 md:col-span-8">
        {/* header bar */}
        <div className="space-x-4 flex flex-wrap bg-white p-5 items-center mb-5 rounded-sm">
          <AiOutlineStar className="h-6 w-6 text-red-500" />
          <h3 className="font-semibold text-black text-sm">
            Jobs that may suit you fields
          </h3>
          <span className="text-gray-500">(8 jobs)</span>
        </div>

        {/* card deck */}
        <div className="grid md:grid-cols-2 gap-5 mb-5 rounded-sm">
          <JobCard jobTitle="Writer"
            logoUrl="https://unsplash.it/40/40"
            company="toxify-inc"
            location="cairo, ain shams"
            ageRange="18-35"
            date="9 days ago"
          />

          <JobCard jobTitle="Marketing"
            logoUrl="https://unsplash.it/40/40"
            company="loop"
            location="cairo, ain shams"
            ageRange="18-35"
            date="9 days ago"
          />

          <JobCard jobTitle="Busness Manager"
            logoUrl="https://unsplash.it/40/40"
            company="toxify-inc"
            location="cairo, ain shams"
            ageRange="18-35"
            date="9 days ago"
          />

          <JobCard jobTitle="Engineer"
            logoUrl="https://unsplash.it/40/40"
            company="toxify-inc"
            location="cairo, ain shams"
            ageRange="18-35"
            date="9 days ago"
          />
        </div>

        {/* Job application history */}
        <div className="bg-white mb-5">
          <h3 className="font-semibold p-5 rounded-sm">
            List of jobs you have applied on
            <span className="font-extralight text-gray-500"> (4) jobs</span>
          </h3>

          <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
              <thead className="text-xs text-gray-700 uppercase  dark:bg-gray-700 dark:text-gray-400">
                <tr>
                  <th scope="col" className="px-6 py-3">
                    Job Title
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Company
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Applicans
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Status
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Application Date
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr className="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                  <th
                    scope="row"
                    className="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    IOS Developer
                  </th>
                  <td className="px-6 py-3">Apple</td>
                  <td className="px-6 py-3">83</td>
                  <td className="px-6 py-3">rejected</td>
                  <td className="px-6 py-3">2 weeks ago </td>
                </tr>
                <tr className="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
                  <th
                    scope="row"
                    className="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    AI Developer
                  </th>
                  <td className="px-6 py-3"> OpenAI</td>
                  <td className="px-6 py-3">350</td>
                  <td className="px-6 py-3"> Noticed</td>
                  <td className="px-6 py-3"> 9 days ago </td>
                </tr>
                <tr className="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                  <th
                    scope="row"
                    className="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    Pianist
                  </th>
                  <td className="px-6 py-3">MurderInc</td>
                  <td className="px-6 py-3">30</td>
                  <td className="px-6 py-3">---</td>
                  <td className="px-6 py-3">1 hour ago </td>
                </tr>
                <tr className="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
                  <th
                    scope="row"
                    className="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    Photographer
                  </th>
                  <td className="px-6 py-3">Pink Moon</td>
                  <td className="px-6 py-3">12</td>
                  <td className="px-6 py-3">accepted</td>
                  <td className="px-6 py-3">3 days ago</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div className="col-span-12 md:col-span-4 space-y-5">
        <div className="space-x-4 flex bg-white p-5 items-center ">
          <span className="">
            You have <span className="font-semibold">(15 jobs)</span> to apply into it this week
          </span>
        </div>

        <div className=" bg-white ">
          <Accordion header="this text don't panic">
            
            <div className="grid grid-cols-12 gap-4">
              <figure className="col-span-4 rounded-md bg-slate-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
              <figure className="col-span-4 rounded-md bg-red-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
              <figure className="col-span-4 rounded-md bg-blue-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
              <figure className="col-span-4 rounded-md bg-green-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
              <figure className="col-span-4 rounded-md bg-yellow-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
              <figure className="col-span-4 rounded-md bg-stone-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
              <figure className="col-span-4 rounded-md bg-orange-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
              <figure className="col-span-4 rounded-md bg-lime-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
              <figure className="col-span-4 rounded-md bg-indigo-400 w-full h-16 ">&<img src="https://unsplash.it" alt="" /></figure>
            </div>
          </Accordion>

          <Accordion header="Fist Question" >
            <div></div>
          </Accordion>

          <Accordion header="Fist Question" >
            <div></div>
          </Accordion>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
