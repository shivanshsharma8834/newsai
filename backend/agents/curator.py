import datetime
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

class CuratorAgent:

    def __init__(self):
        pass

    def curate_sources(self, query: str, sources: list):

        message = [{
            "role" : "system",
            "content" : """ You are a professional newspaper editor. Your sole purpose is 
            to choose 5 most relevant articles for me to read from a list of articles."""
        }, {
            "role" : "user",
            "content" : f""" Today's date is {datetime.now().strftime('%d/%m/%Y')}\n."
                       f"Topic or Query: {query}\n"
                       f"Your task is to return the 5 most relevant articles for me to read for the provided topic or "
                       f"query\n "
                       f"Here is a list of articles:\n"
                       f"{sources}\n"
                       f"Please return nothing but a list of the strings of the URLs in this structure: ['url1',"
                       f"'url2','url3','url4','url5'].\n "

            """
        }]

        llm = ChatGroq(
            api_key=os.environ.get("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
        )

        response = llm.invoke(message)

        return response
    

    def run(self, article : dict):
        article["sources"] = self.curate_sources(article["query"], article["sources"])
        return article