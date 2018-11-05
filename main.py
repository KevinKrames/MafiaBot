from fbchat import Client, log
from pymongo import MongoClient
import json
from pprint import pprint
import os
from DatabaseManager import DatabaseManager
from Game import Game

databaseManager = DatabaseManager()

game = Game().Run()


# class EchoBot(Client):
#     def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
#         self.markAsDelivered(thread_id, message_object.uid)
#         self.markAsRead(thread_id)

#         log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
    
#         if author_id != self.uid:
#             self.send(message_object, thread_id=thread_id, thread_type=thread_type)


# client = EchoBot(data["username"], data["password"])
# client.listen()