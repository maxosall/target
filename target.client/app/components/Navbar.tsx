"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import React, { useEffect, useState } from "react";
import { AiOutlineMenu } from "react-icons/ai";
import { BiTargetLock } from "react-icons/bi";

export const Navbar = () => {
  const currentPath = usePathname()

  const [isActive, setIsActive] = useState(false);
  useEffect(() => {
    toggleMenu;
  }, [isActive]);
  const toggleMenu = () => (isActive == true ? "flex" : "hidden");

  const links = [
    { label: "Dashboard", href: "/dashboard" },
    { label: "Job Opennings", href: "/job-opennings" },
    { label: "Browse Jobs", href: "/browse-job" },
    { label: "Profile", href: "/account/profile" },
  ];

  return (
    <nav className="bg-white border-gray-200 dark:bg-gray-900 border-b mb-5">
      <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
        <Link href="/dashboard" className="flex items-center space-x-4">
          <BiTargetLock className="h-9 w-9 text-red-500 hover:text-red-700 "></BiTargetLock>
          <span className="self-center text-lg text-red-500 hover:text-red-700 font-extrabold whitespace-nowrap dark:text-white">
            target
          </span>
        </Link>

        <div className="flex items-center md:order-2 space-x-2">
          <Link
            href="/account/signup"
             className="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-semibold rounded-md text-sm px-3 py-2 mr-3 md:mr-0  dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700">
            Sign up
            </Link>
          <Link
            href="/account/login"
            className="text-white font-semibold bg-gray-800 hover:bg-gray-900 focus:ring-4 focus:outline-none focus:ring-blue-300 font-sm rounded-md text-sm px-3 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Login
          </Link>
          <button
            data-collapse-toggle="navbar-cta"
            type="button"
            className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-md md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
            aria-controls="navbar-cta"
            aria-expanded="false"
          >
            <span className="sr-only">Open main menu</span>
            <AiOutlineMenu
              onClick={() => setIsActive(!isActive)}
              className="w-6 h-6 text-gray-900 font-light text-sm"
            />
          </button>
        </div>
        <div
          className={`${toggleMenu()} items-center justify-between w-full md:flex md:w-auto md:order-1 `}
          id="navbar-cta"
        >
          {/* <ul className="w-full flex flex-col font-normal text-sm p-4 md:p-0 mt-4 border border-gray-100 rounded-md bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"> */}
          <ul className="w-full flex flex-col font-normal text-sm p-4 md:p-0 mt-4 rounded-md bg-white md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
            {links.map((link) => (
              <li>
                <Link
                  className={`${link.href == currentPath 
                    ? 'text-blue-800 font-semibold underline-offset-8 underline' 
                    : 'text-gray-900'} 
                  block pl-3 pr-4 py-2 rounded-md hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700`}
                  key={link.href}
                  href={link.href}
                >
                  {" "}
                  {link.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </nav>
  );
};
