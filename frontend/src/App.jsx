import { useState } from "react"


function App() {

  const [inputValue , setInputValue] = useState('');
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch('http://127.0.0.1:5000/generate_newspaper', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic: inputValue }),
      });
      
      if (!res.ok) throw new Error(`HTTP error! Status: ${res.status}`);
      
      const data = await res.json();
      setResponse(data);
      setError(null);
      setInputValue('');
    } catch (err) {
      setError(err.message);
      setResponse(null);
    }


  }
  
  return (
    <div className="bg-blue-400">
      <form onSubmit={handleSubmit}> 
        <input
        type="text"
        name="topic"
        value={inputValue} 
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Enter news topic"
        />
        <button type="submit">Submit</button>
      </form>
      {response && <div>
        Response: {
          JSON.stringify(response)
        }
      </div>}

      {error && <div>
        Error: {
          error
        }  
      </div>}
    </div>
  )
}

export default App
