from ast import List
import json
import os
import time
from typing import Dict, TypedDict
from flask import Flask, jsonify, request
from flask_cors import CORS
from langgraph.graph import Graph, START, END
from agents.search import SearchAgent
from agents.curator import SourceCuratorAgent
from agents.scrapper import WebScrapperAgent




class MasterAgent:


    def __init__(self):
        self.outputDir = f"output/run_{int(time.time())}"
        os.makedirs(self.outputDir, exist_ok=True)

    def run(self, topics: List):

        workflow = Graph()
        
        searchAgent = SearchAgent()
        sourceCuratorAgent = SourceCuratorAgent()
        scrapperAgent = WebScrapperAgent()

        workflow.add_node("search", searchAgent.run)
        workflow.add_node("source_curate", sourceCuratorAgent.run)
        workflow.add_node("web_scrapper", scrapperAgent.run)

        workflow.add_edge(START, "search")
        workflow.add_edge("search", "source_curate")
        workflow.add_edge("source_curate", "web_scrapper")
        workflow.add_edge("web_scrapper", END)
        
        chain = workflow.compile()

        result = {"query" : topics[0]}
        chain.invoke(result)

        return result






backendApp = Flask(__name__)
CORS(backendApp)

@backendApp.route('/', methods=['GET'])
def index():
    return jsonify({"status" : "Running"}), 200

@backendApp.route('/generate_newspaper', methods=['POST'])
def generate_newspaper():
    data = request.json
    print("JSON data: ", data)
    print(type(data))
    topics = data["topic"].split(",")
    masteragent = MasterAgent()
    result = masteragent.run(topics)
    response = jsonify({"message" : result })
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")

    return response 
