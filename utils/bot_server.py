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
        running_bot = ""
        while True:
            conn, address = server.accept()  # Establish connection with client.
            print("server listening at" + str(address))
            data = conn.recv(1024)
            name = data.decode()
            running_bot = name
            print("running_bot" + running_bot)

            if running_bot != "xxx":
                utils.bot_client.run_bot(running_bot)
