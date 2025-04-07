# NewsAI - AI-Powered News Aggregator 

**NewsAI** is a modern news aggregator tool that utilizes LLMs to curate and summarize news articles from various sources on the web, providing the users with a personalized and efficient way to stay updated. 

# Features 

- **AI-Powered Summaries** - Get concisre summaries of news articles using latest LLM models (Lllama, ChatGPT, Deepseek).
- **Multi-Source Aggregation** - Fetch news from multiple APIs (NewsAPI, GNews, etc).
- **Personalized Feed** - Customize news preferences based on categories (tech, sports, business, etc).
- **Search Functionality** - Find news articles by keywords or topics.
- **Multi agentic application** - The Application uses dedicated AI agents create 

# Technologies Used 

- **Frontend**: React.js, TailwindCSS
- **Backend**: Flask, FastAPI
- **AI Integration**: Groq API (Llama 3.2, DeepSeek)
- **LLM Framework**: Groq, LangChain, LangGraph
- **NewsAPI**: Tavily
- **Deployment**: Vercel (Frontend), Render/Heroku (Backend)

# Installation & Setup

- Clone the repository
```
git clone https://github.com/shivanshsharma8834/newsai.git
cd newsai
```

- Install Python dependencies
```
uv install 
```

- Set up environment variables
Create a .env file in the root directory with the following
```
TAVILY_API_KEY=your api key
GROQ_API_KEY=your api key
OPENAI_API_KEY=your api key
```

# Running the frontend 

- Install node dependencies
```
cd frontend
bun install 
```

- Run the server
```
bun run dev
```

# Running the backend 

- Run the server
```
cd backend
flask --app server run 
```


# Contributing 

Contributions are welcomed! Feel free to open an issue or submit a PR. 

- Fork the repository

- Create a new branch (git checkout -b feature/xyz)

- Commit your changes (git commit -m "Add feature xyz")

- Push to the branch (git push origin feature/xyz)

- Open a Pull Request

# License

This project is licenced under the **MIT License**

# This is a learning project. 
Made with <3 by @shivanshsharma8834
   



