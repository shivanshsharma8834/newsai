import { useEffect, useState } from 'react'
import Font from 'react-font'

export default function Header() {

    const [currentDate, setCurrentDate] = useState('');

    const updateDate = () => {
        const now = new Date();
        const formattedDate = now.toLocaleDateString('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
        setCurrentDate(formattedDate)
    }

    useEffect(() => {
        updateDate();
    }, []);
    return (
        <div className="w-full h-[165px] flex justify-center relative border-b-4 mb-2 border-amber-900">
            <Font family='Grenze Gotisch' >
                <h1 className='text-amber-900 text-[75px]'>La Plume Électronique</h1>
                <p className='text-[25px] text-amber-900 absolute left-20'>{currentDate}</p>
            </Font>
        </div>
    )
}