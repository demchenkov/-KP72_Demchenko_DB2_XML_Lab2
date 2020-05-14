from random import randrange
from time import sleep


class MessageHandler:
    def __init__(self):
        pass

    def is_message_valid(self, message: str):
        return randrange(100) > 10
