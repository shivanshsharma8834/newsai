import os
from dotenv import load_dotenv
from tavily import TavilyClient





class SearchAgent:

    def __init__(self):
        load_dotenv()
        self.tavilyAgent = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
    
    def search_tavily(self, query: str):

        results = self.tavilyAgent.search(query=query, topic="news", max_results=10, include_images=True)
        sources = results["results"]
        try:
            image = results["images"][0]
        except:
            image = "https://picsum.photos/800/600"

        return sources, image
    
    def run(self, article: dict):
        res = self.search_tavily(article["query"])
        article["sources"] = res[0]
        article["image"] = res[1]

        return article