"""gui runner application for the osrs-python-bot api"""
import customtkinter
from frames.bot_key_frame import BotKeyFrame
from frames.bot_list_frame import BotListFrame
from frames.action_buttons_frame import ActionButtonsFrame
from utils.bot_server import TCPServer

class App(customtkinter.CTk):
    """main application"""
    def __init__(self):
        """main application frames and grid"""
        super().__init__()
        self.title("osrs-bots")
        self.grid_columnconfigure(0, weight=4)
        self.grid_rowconfigure(0, weight=1)

        self.bot_key_frame = BotKeyFrame(self)
        self.bot_key_frame.grid(row=0, column=0, padx=10, pady=10, sticky="sew")

        self.bot_list_frame = BotListFrame(self, title="Select a Bot")
        self.bot_list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="sew")
        self.action_buttons_frame = ActionButtonsFrame(
            self,
            self.bot_key_frame,
            self.bot_list_frame
        )
        self.action_buttons_frame.grid(row=2, column=0, padx=10, pady=10, sticky="sew")


# TCP SERVER (BOT RUNNER)
server = TCPServer()
server.daemon = True # close the TCPServer when the main thread (GUI) exits
server.start() # start the thread

# APPLICATION (GUI)
app = App()
app.mainloop()
