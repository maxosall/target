import { useEffect, useState } from "react"

interface IAccordionProrps{
  header: string
  children: React.ReactNode[]
  className?: string
}
export const Accordion = ({className, header, children}: IAccordionProrps) => {
  const [isActive, setIsActive] = useState(false)
  useEffect(() => {toggleAccordion}, [isActive])
  const toggleAccordion = () => isActive == true ? 'block' : "hidden"
  

  return (
    <div>
      <h3  onClick={() => setIsActive(!isActive)} className={`p-5 text-sm font-semibold cursor-pointer border-b ${className}`}>
        {header}</h3>
      <div className={`p-5 ${toggleAccordion()}`}>
        { children }
      </div>
    </div>
  )

  
}
