import React from 'react'

export const Badge = ({bgColor, color, text='new'}) => {
  return (
    <span className={`bg-${bgColor}-100 text-${color}-800 text-xs 
    font-medium mr-2 px-2.5 py-0.5 rounded 
    dark:bg-${bgColor}-900 dark:text-${color}-300`}>{text}</span>

  )
}
