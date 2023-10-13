import React from 'react'
import { SearchBox } from '../components/SearchBox'
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
            <ul>
              {/* {filter_list.map(f_list => <li key={f_list.id}>
                
              </li>)} */}
            </ul>
          </aside>

        </div>
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