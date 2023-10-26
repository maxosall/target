import React from 'react'
import { SearchBox } from '../components/SearchBox'
import { JobBar } from '../components/JobBar'
const JobOpennings = () => {
  const filter_list = [
    {'id':1, 'contries': ['senegal', 'mali', 'france', 'usa', 'uk', 'egypt']},
    {'id':2,'education level': ['all', 'none', 'high education']},
    {'id':3, 'industry': ['software development', 'office', 'music', 'finance']},
    {'id':4,'gender': ['male', 'female']}
  ]  
  return (
    <div className='grid grid-cols-12 space-y-5 md:space-y-0 md:space-x-5 '>
      <div className="col-span-12 md:col-span-3">
        <div className='bg-white'>
          <h3 className='font-semibold p-5 text-gray-700'>Enhence your search</h3>
          <aside className='px-5'>
            
          </aside>

        </div>
      </div>
      <div className='col-span-12 md:col-span-9 space-y-5'>
        <div className='p-5 bg-white '>
          <SearchBox />
        </div>
        <div className=''>
          <JobBar jobTitle='.NET Development' 
            posted_date='2 days ago' 
            company='loop inc' 
            location='senegal, dakar, parcel unit 2' 
            minSalary='5400000' />
            
          <JobBar jobTitle='Writer' 
            posted_date='6 days ago' 
            company='the sun' 
            location='senegal, dakar, parcel unit 2' 
            minSalary='5400000' />
            
          <JobBar jobTitle='.NET Development' 
            posted_date='2 days ago' 
            company='loop inc' 
            location='senegal, dakar, parcel unit 2' 
            minSalary='5400000' />

          <JobBar jobTitle='Marketing' 
            posted_date='2 days ago' 
            company='BMC' 
            location='senegal, dakar, parcel unit 2' 
            minSalary='5400000' />

          <JobBar jobTitle='.NET Development' 
            posted_date='2 days ago' 
            company='loop inc' 
            location='senegal, dakar, parcel unit 2' 
            minSalary='5400000' />

          <JobBar jobTitle='Securtary Exsecutive' 
            posted_date='2 days ago' 
            company='loop inc' 
            location='senegal, dakar, parcel unit 2' 
            minSalary='5400000' />
        </div>
      </div>
    </div>
  )
}

export default JobOpennings