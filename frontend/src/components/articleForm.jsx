import { useState } from "react";
import ArticleContent from "./articleContent";

export default function ArticleForm() {

    const [inputTopic, setInputTopic] = useState('');
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await fetch('http://127.0.0.1:5000/generate_newspaper', {
                method: 'POST',
                headers: {'Content-Type' : 'application/json'},
                body: JSON.stringify({ topic : inputTopic }),
            })

            if (!res.ok) throw new Error(`HTTP error! Status : ${res.status}`);

            const data = await res.json();
            setResponse(data);
            setError(null);
            setInputTopic('');
        } catch (err) {
            setError(err.message);
            setResponse(null);
        }
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input 
                type="text"
                name="topic"
                value={inputTopic}
                onChange={(e) => setInputTopic(e.target.value)}
                placeholder="Enter news topic"
                />
                <button type="submit">Submit</button>
            </form>
            {
                response && <ArticleContent response={response}/>
            }

            {error && <div>
                Error: {
                error
                }  
            </div>}
        </div>
    )

}