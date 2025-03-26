import ast
from datetime import datetime
import json
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv


class SourceCuratorAgent:

    def __init__(self):
        load_dotenv()
        self.llm = ChatGroq(
            api_key=os.environ.get("GROQ_API_KEY"),
            model="llama-3.2-3b-preview",
        )

    def curate_sources(self, query: str, sources: list):

        message = [{
            "role" : "system",
            "content" : """ You are a professional newspaper editor. Your sole purpose is 
            to choose 3 most relevant articles for me to read from a list of articles.
            Please return nothing but a list of the strings of the URLs in this structure: ['url1','url2','url3','url4','url5']."""
        }, {
            "role" : "user",
            "content" : f""" Today's date is {datetime.now().strftime('%d/%m/%Y')}\n
                       Topic or Query: {query}\n
                       Your task is to return the 5 most relevant articles for me to read for the provided topic or query\n
                       Here is a list of articles:\n
                       {sources}\n
                       Please return nothing but a list of the strings of the URLs in this structure: ['url1','url2','url3','url4','url5'].\n "

            """
        }]

        

        response = self.llm.invoke(message)

        return response.content
    

    def run(self, article : dict):
        article["sources"] = self.curate_sources(article["query"], article["sources"])
        article["sources"] = ast.literal_eval(article["sources"])
        return article