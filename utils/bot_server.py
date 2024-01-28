"""server that runs the bots so that the gui is not bogged down with the thread running the bot"""
from threading import Thread
import socket
import utils.bot_client

class TCPServer(Thread):
    """tcp server configuration extending Thread"""
    def __init__(self):
        self.data = {} # initial data value
        super().__init__()

    def run(self):
        """main run loop for the tcp server"""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", 3363))
        server.listen(1)
        bot = ""

        while True:
            conn, address = server.accept()
            print("server listening at" + str(address))
            data = conn.recv(1024)

            selected_bot_and_key = data.decode().split("/")
            bot = selected_bot_and_key[0]
            key = selected_bot_and_key[1]

            print("checking " + key + " for access")
            # THIS IS WHERE THE GOLDEN BOT KEY NEEDS TO BE VALIDATED

            if bot != "xxx":
                utils.bot_client.run_bot(bot, key)
