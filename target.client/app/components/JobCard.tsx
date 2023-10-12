import React from 'react'

export const JobCard = ({jobTitle, logoUrl, compnay, location, date, ageRange}) => {
  return (
    
  <div  className="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
    {/* card header */}
    <div className='flex justify-between'>
      <h3>{jobTitle}</h3>
      <img src={logoUrl} />
    </div>

    <div className=''>
      <p>{compnay}</p>
      <p>{location}</p>
      <p className='flex justify-between'>{date} . {ageRange}</p>
    </div>
    <button className=''>apply now</button>
  </div>

  )
}
