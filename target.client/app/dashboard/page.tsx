import React from 'react'
import { AiOutlineStar } from "react-icons/ai"
import { JobCard } from '../components/JobCard'

const Dashboard = () => {
  return (
    <div className='grid grid-cols-12 space-y-5 md:space-y-0 md:space-x-5 '>
      <div className='col-span-12 md:col-span-8'>

        {/* header bar */}
        <div className='space-x-4 flex flex-wrap bg-white p-5 items-center mb-5'>
          <AiOutlineStar className='h-8 w-8' />
          <h3 className='font-bold'>Jobs that may suit you fields</h3>
          <span className='text-gray-500'>(8 jobs)</span>
        </div>

        {/* card deck */}
        <div className="grid md:grid-cols-2 gap-5 mb-5">
          <JobCard jobTitle='Data Entry' logoUrl='https://unsplash.it/40/40'
            compnay='toxify-inc'
            location='cairo, ain shams'
            ageRange='18-35'
            date='9 days ago' />

          <JobCard jobTitle='Data Entry' logoUrl='https://unsplash.it/40/40'
            compnay='toxify-inc'
            location='cairo, ain shams'
            ageRange='18-35'
            date='9 days ago' />

          <JobCard jobTitle='Data Entry' logoUrl='https://unsplash.it/40/40'
            compnay='toxify-inc'
            location='cairo, ain shams'
            ageRange='18-35'
            date='9 days ago' />
          <JobCard jobTitle='Data Entry' logoUrl='https://unsplash.it/40/40'
            compnay='toxify-inc'
            location='cairo, ain shams'
            ageRange='18-35'
            date='9 days ago' />
        </div>

        {/* Job application history */}
        <div className="bg-white mb-5">
          <h3 className='font-semibold p-5'>List of jobs you have applied on
            <span className='font-extralight text-gray-500'> (4) jobs</span>
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
                  <th scope="row" className="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    IOS Developer
                  </th>
                  <td className="px-6 py-3">
                    Apple
                  </td>
                  <td className="px-6 py-3">
                    83
                  </td>
                  <td className="px-6 py-3">
                    rejected
                  </td>
                  <td className="px-6 py-3">2 weeks ago </td>
                </tr>
                <tr className="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
                  <th scope="row" className="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    AI Developer
                  </th>
                  <td className="px-6 py-3"> OpenAI
                  </td>
                  <td className="px-6 py-3">
                    350
                  </td>
                  <td className="px-6 py-3"> Noticed
                  </td>
                  <td className="px-6 py-3"> 9 days ago </td>
                </tr>
                <tr className="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                  <th scope="row" className="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    Pianist
                  </th>
                  <td className="px-6 py-3">
                    MurderInc
                  </td>
                  <td className="px-6 py-3">
                    30
                  </td>
                  <td className="px-6 py-3">
                    ---
                  </td>
                  <td className="px-6 py-3">1 hour ago                  </td>
                </tr>
                <tr className="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
                  <th scope="row" className="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    Photographer
                  </th>
                  <td className="px-6 py-3">
                    Pink Moon
                  </td>
                  <td className="px-6 py-3">
                    12
                  </td>
                  <td className="px-6 py-3">
                    accepted
                  </td>
                  <td className="px-6 py-3">3 days ago</td>
                </tr>

              </tbody>
            </table>
          </div>

        </div>

      </div>
      <div className='col-span-12 md:col-span-4'>
        <div className='space-x-4 flex bg-white p-5 items-center '>
          <span className=''>You have <span className='font-semibold'>(15 jobs)</span> to apply into it this week</span>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
