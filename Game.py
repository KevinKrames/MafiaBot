import json
from pymongo import MongoClient
from pprint import pprint
import sched, time
import os
from DatabaseManager import DatabaseManager
from MessengerBot import MessengerBot

credentials = os.path.abspath('credentials.json')

class Game:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        with open(credentials) as f:
            data = json.load(f)
        self.messengerBot = MessengerBot(data["username"], data["password"])
        self.databaseManager = DatabaseManager()

    def Run(self):
        self.scheduler.enter(10, 1, Game.Update, argument=(self,))
        self.messengerBot.listen()
        self.scheduler.run()

    def Update(self):
        print("test")
        # Check for timed events

        # Update Events

        # Log events to Database

        # Send Messages

        # Log Messages Sent To Database

        # Rerun update method
        self.scheduler.enter(10, 1, Game.Update, argument=(self,))