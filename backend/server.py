from ast import List
import json
import os
import time
from typing import Dict, TypedDict
from flask import Flask, jsonify, request
from flask_cors import CORS
from langgraph.graph import Graph, START, END
from agents import search
from backend.agents.curator import CuratorAgent




class MasterAgent:


    def __init__(self):
        self.outputDir = f"output/run_{int(time.time())}"
        os.makedirs(self.outputDir, exist_ok=True)

    def run(self, topics: List):

        workflow = Graph()
        
        searchAgent = search.SearchAgent()
        curatorAgent = CuratorAgent()

        workflow.add_node("search", searchAgent.run)
        workflow.add_edge(START, "search")
        workflow.add_edge("search", END)
        
        chain = workflow.compile()
        chain.invoke({"query" : topics[0]})






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
    topics = data["topic"].split()
    masteragent = MasterAgent()
    masteragent.run(topics)
    response = jsonify({"message" : "Done"})
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")

    return response 
# main()
