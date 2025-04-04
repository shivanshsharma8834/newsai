from datetime import datetime

class WriterAgent:

    def __init__(self):
        pass

    def write_article(self, query : str, sources : list):

        message = [{
            "role" : "system",
            "content" : """ You are a professional newspaper writer. Your sole purpose is 
            to choose 3 most relevant articles for me to read from a list of articles.
            Please return nothing but a list of the strings of the URLs in this structure: ['url1','url2','url3']."""
        }, {
            "role" : "user",
            "content" : f""" Today's date is {datetime.now().strftime('%d/%m/%Y')}\n
                       Topic or Query: {query}\n
                       Your task is to return the 3 most relevant articles for me to read for the provided topic or query\n
                       Here is a list of articles:\n
                       {sources}\n
                       Please return nothing but a list of the strings of the URLs in this structure: ['url1','url2','url3'].\n "

            """
        }]