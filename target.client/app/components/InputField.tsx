import React from 'react'

interface InputFieldProps{
  label:string;
  type:string;
  placeholder?:string;
  htmlFor:string
}
export const InputField = ({label, htmlFor, type, placeholder}: InputFieldProps) => {
  return (
    <div className='pb-4'>
     <label className='block font-semibold text-sm ' htmlFor={htmlFor}>{label}</label> 
     <input className='rounded-md w-full text-sm p-2' type={type} placeholder={placeholder} id={htmlFor}/>
    </div>
  )
}
