# -*- coding: UTF-8 -*-

from fbchat import Client, log
import json
from pprint import pprint
import os

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

path = os.path.abspath('credentials.json')
with open(path) as f:
    data = json.load(f)

client = EchoBot(data["username"], data["password"])
client.listen()