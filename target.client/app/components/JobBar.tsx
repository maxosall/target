import React from 'react'
import { Badge } from './Badge'

export const JobBar = ({jobTitle, posted_date, company, location, minSalary}) => {
  return (
    <div className='p-5 bg-white w-full flex justify-between border-b'>
      <div className='space-y-2'>
        <div className='flex items-center flex-wrap space-x-2'>
          <h3 className='font-bold text-lg'>{jobTitle}</h3>
          <Badge bgColor="blue" color="blue" />
          <span className='text-xs font-medium'>{posted_date}</span>
        </div>

        <div className='flex'>
          <h5 className='font-medium'> {company} </h5> . 
          <span> {location}</span>
        </div>

        <div className="flex">
          <p className='font-medium'>Basic Salary: </p>
          <span>{minSalary}</span>
        </div>
      </div>
      <img src='https://unsplash.it/100/100' />
    </div>
  )
}