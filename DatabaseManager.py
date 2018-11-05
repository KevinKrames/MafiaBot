import json
from pymongo import MongoClient
from pprint import pprint
import os

credentials = os.path.abspath('credentials.json')

class DatabaseManager:
    def __init__(self):
        with open(credentials) as f:
            data = json.load(f)

            client = MongoClient(data["dbkey"] + data["dbdatabase"])
            mydatabase = client[data["dbdatabase"]] 

            self.collection = mydatabase["Testing"]

    def InsertRecord(self, record):
        self.collection.insert_one(record)

# record example
# rec = { 
#     "title": 'MongoDB and Python',  
#     "description": 'MongoDB is no SQL database',  
#     "tags": ['mongodb', 'database', 'NoSQL'],  
#     "viewers": 104 
# }