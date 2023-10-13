import React from 'react'
import { AiOutlineStar } from "react-icons/ai"
import { JobCard } from '../components/JobCard'

const Dashboard = () => {
  return (
    <div className='grid grid-cols-12 space-y-5 md:space-y-0 md:space-x-5 '>
      <div className='col-span-12 md:col-span-8'>

        {/* header bar */}
        <div className='space-x-4 flex bg-white p-5 items-center mb-5'>
          <AiOutlineStar className='h-8 w-8' />
          <h3 className='font-bold'>Jobs that may suit you fields</h3>
          <span className='text-gray-500'>(8 jobs)</span>
        </div>

        {/* card deck */}
        <div className="grid md:grid-cols-2 gap-5">
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
