import json
from pymongo import MongoClient
from pprint import pprint
import sched, time
import os
from MessengerBot import MessengerBot

credentials = os.path.abspath('credentials.json')

class Game:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.messengerBot = MessengerBot(data["username"], data["password"])

    def Run(self):
        self.scheduler.enter(10, 1, Game.Update, argument=(self,))
        self.scheduler.run()

    def Update(self):
        print("test")
        # Check for timed events

        # Update Events

        # Send Messages

        # Log Messages Sent To Database

        # Rerun update method
        self.scheduler.enter(10, 1, Game.Update, argument=(self,))