import React from 'react'
import {AiOutlineStar} from "react-icons/ai"
const Dashboard = () => {
  return (
    <div className='grid grid-cols-12 space-x-5'>
      <div className='col-span-8'>


        <div className='space-x-4 flex bg-white p-5 items-center '>
          <AiOutlineStar className='h-8 w-8'/> 
          <h3 className='font-bold'>Jobs that may suit you fields</h3>
          <span className='text-gray-500'>(8 jobs)</span>
        </div>


      </div>
      <div className='col-span-4'>
      <div className='space-x-4 flex bg-white p-5 items-center '>
          <span className=''>You have <span className='font-semibold'>(15 jobs)</span> to apply into it this week</span>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
