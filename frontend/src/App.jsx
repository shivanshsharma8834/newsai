import { useState } from "react"
import Header from "./components/header";
import ArticleForm from "./components/articleForm";
import Footer from "./components/footer";


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

    <div className="bg-yellow-200 h-full">
      <Header/>
      <ArticleForm/>
      <Footer/>
    </div>
  )
}

export default App
