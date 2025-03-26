from ast import Dict
from calendar import c
import concurrent.futures
from unittest import result
from urllib import response
from bs4 import BeautifulSoup
import concurrent
from httpx import head
from langchain_groq import ChatGroq
import requests


class WebScrapperAgent:

    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.2,
            model="llama-3.3-70b-versatile"
        ) 
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' 
        }

    def fetch_html(self, url : str):
        """Fetch the html text from the url"""
        try:
            response = requests.get(url ,headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f'Error fetching {url}: {str(e)}')
            return ""

    def parse_article(self, html : str):
        """Extract the article content from the url header"""
        soup = BeautifulSoup(html, 'html.parser')

        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()

        article = soup.find('article') or soup.find('main') or soup.body
        return article.get_text(separator='\n', strip=True) if article else ""
    
    def curate_content(self, text: str):
        """Curate an article content"""
        message = [{
            "role" : "system",
            "content" : """ You are a professional content curator. Extract and structure key
            information from the provided article text. Return only JSON with the following structure:

            {
                "title": "Article title",
                "author": "Author name if available",
                "publish_date": "Publication date if available",
                "summary": "3-sentence summary",
                "key_points": ["list", "of", "main points"],
                "keywords": ["list", "of", "important keywords"]
            }

            """
        }, 
        {
            "role" : "user",
            "content" : f"Article content: {text}"
        }]

        return self.llm.invoke(message).content


        

    def process_url(self, url: str):
        """ Process a single URL """
        html = self.fetch_html(url)    
        if not html:
            return {"url" : url, "error" : "Failed to fetch component"}
        
        clean_text = self.parse_article(html)
        if not clean_text.strip():
            return { "url" : url, "error" : "No content extracted"}
        
        try:
            curated = self.curate_content(clean_text)
            return {"url" : url, "data" : curated}
        except Exception as e:
            return {"url" : url, "error" : f"Curation failed: {str(e)}"}
        
    def run(self, article : Dict):
        """Run the scrapper agent"""
        urls = article['sources']
        result = None
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(self.process_url, url) for url in urls]
            result = [future.result() for future in concurrent.futures.as_completed(futures)]

        article['curated_articles'] = result 
        return article
           

            