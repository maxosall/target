import Link from 'next/link'
import React from 'react'
import { AiOutlineMenu } from 'react-icons/ai';
import {BiTargetLock } from 'react-icons/bi';
export const Navbar = () => {
  const links = [
    {'label': 'Dashboard', 'href': '/dashboard'},
    {'label': 'Job Opennings', 'href': '/job-opennings'},
    {'label': 'Browse Jobs', 'href': '/job-browse'},
    {'label': 'Profile', 'href': 'profile'}
  ]

  return (
    
<nav className="bg-white border-gray-200 dark:bg-gray-900 border-b mb-5">
  <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
  <a href="/dashboard" className="flex items-center space-x-4">
      <BiTargetLock className="h-9 w-9 text-red-500 hover:text-red-700 "></BiTargetLock>
      <span className="self-center text-lg text-red-500 hover:text-red-700 font-black whitespace-nowrap dark:text-white">target</span>
  </a>
  <div className="flex items-center md:order-2 space-x-2">
      <button type="button" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-sm rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        Sign up</button>
        <button type="button" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-sm rounded-lg text-sm px-4 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        Login</button>
      <button data-collapse-toggle="navbar-cta" type="button" className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-cta" aria-expanded="false">
        <span className="sr-only">Open main menu</span>
        <AiOutlineMenu className="w-6 h-6 text-gray-900" />
    </button>
  </div>
  <div className="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-cta">
    <ul className="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
     
     {links.map(link => <li><Link className=' block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700'
      key={link.href} href={link.href} > { link.label }</Link>
      </li>)}
     
    </ul>
  </div>
  </div>
</nav>

  )
}
