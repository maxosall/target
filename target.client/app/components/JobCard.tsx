import React from 'react'
import {IoLocationOutline} from 'react-icons/io5'
import { CgCalendarDates } from 'react-icons/cg'
export const JobCard = ({jobTitle, logoUrl, compnay, location, date, ageRange}) => {
  return (
    
  <div  className="block space-y-5 md:max-w-md p-6 bg-white border border-gray-200 rounded-md shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
    {/* card header */}
    <div className='flex justify-between '>
      <h3 className='font-bold'>{jobTitle}</h3>
      <img className='rounded-full' src={logoUrl} />
    </div>

    <div className=''>
      <p className='flex space-x-4 items-center'>Company: <span className='font-semibold'> {compnay}</span></p>
      <p className='flex space-x-4 items-center'><IoLocationOutline /><span>{location}</span></p>
      <p className='flex justify-between  space-x-4 items-center'> 
        <span className='flex items-center '> 
        <CgCalendarDates />{date} . age range ({ageRange})</span>
      </p>
    </div>
    <button type="button" className="px-5 py-2.5 w-full text-sm font-medium text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-md text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">view description</button>

  </div>

  )
}
