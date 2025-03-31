import { useState } from "react";
import {CircularProgress} from '@heroui/progress'
import ArticleContent from "./articleContent";

export default function ArticleForm() {

    const [inputTopic, setInputTopic] = useState('');
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true)
        try {
            const res = await fetch('http://127.0.0.1:5000/generate_newspaper', {
                method: 'POST',
                headers: {'Content-Type' : 'application/json'},
                body: JSON.stringify({ topic : inputTopic }),
            })

            if (!res.ok) throw new Error(`HTTP error! Status : ${res.status}`);

            const data = await res.json();
            setIsLoading(false)
            setResponse(data);
            setError(null);
            setInputTopic('');
        } catch (err) {
            setError(err.message);
            setResponse(null);
        }
    }

    return (
        <div className="min-h-[750px] mt-3">
            <div className="px-20 flex flex-col">
                <form onSubmit={handleSubmit} className="min-h-[250px] flex flex-col gap-y-3">
                    <input 
                    type="text"
                    name="topic"
                    value={inputTopic}
                    onChange={(e) => setInputTopic(e.target.value)}
                    placeholder="Enter news topics separated by commas"
                    className="h-[100px] w-full pl-3 pt-0 text-left bg-amber-100 border-3 rounded-2xl border-amber-900 focus-within:border-amber-50"
                    />
                    <button type="submit" className="border-amber-900 border-3 h-[50px] rounded-2xl w-[100px] hover:border-amber-200 hover:bg-amber-900 hover:text-amber-200">Submit</button>
                </form>
                {
                    response? (<ArticleContent response={response}/>) : 
                    isLoading? (<div className="flex justify-center items-center">
                        <div className="animate-spin rounded-full h-8 w-8 border-b-3 border-amber-900"></div>
                    </div>) : 
                    (<div></div>)
                }

            </div>
            
            {error && <div>
                Error: {
                error
                }  
            </div>}
        </div>
    )

}