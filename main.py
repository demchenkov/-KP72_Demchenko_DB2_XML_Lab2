import signal
import sys

import npyscreen

from rds.controllers.client import Client
from rds.controllers.message import Message
from tui import auth_view
from tui.admin_view import AdminDisplay
from tui.message_view import MessageListDisplay
from tui.send_message_view import SendMessageDisplay


class App(npyscreen.StandardApp):
    def __init__(self):
        super().__init__()
        signal.signal(signal.SIGINT, self.__handle_interrupt_event)
        signal.signal(signal.SIGTERM, self.__handle_interrupt_event)
        self.client_controller = Client()
        self.message_controller = Message()
        self.username = ''

    def onStart(self):
        self.addForm("MAIN", auth_view.AuthDisplay, name="Auth")
        self.addFormClass("MESS", MessageListDisplay, name="Main")
        self.addFormClass("SEND_MESS", SendMessageDisplay, name="Send Message")
        self.addFormClass("ADMIN", AdminDisplay, name="Admin")

    def __handle_interrupt_event(self, _sig, _frame):
        self.onCleanExit()
        sys.exit(0)

    def onCleanExit(self):
        if isinstance(self.username, str):
            self.client_controller.logout(self.username)


if __name__ == '__main__':
    myApp = App()
    myApp.run()
