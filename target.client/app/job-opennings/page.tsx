import React from 'react'
import { SearchBox } from '../components/SearchBox'
const JobOpennings = () => {
  return (
    <div className='grid grid-cols-12 space-y-5 md:space-y-0 md:space-x-5 '>
      <div className="col-span-12 md:col-span-3">
        side bar
      </div>
      <div className='col-span-12 md:col-span-9'>
        <div className='p-5 bg-white'>
          <SearchBox />
        </div>
      </div>
    </div>
  )
}

export default JobOpennings