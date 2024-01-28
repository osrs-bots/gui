"""frame for the action buttons extending CTkFrame"""
import sys
import socket
import customtkinter

class ActionButtonsFrame(customtkinter.CTkFrame):
    """contains action buttons for starting and stopping bopt"""
    def __init__(self, master, bot_key_frame, bot_list_frame):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        # START BUTTON
        green_color = "#1b5e20"
        self.start_button = customtkinter.CTkButton(
            self,
            text="Start",
            command=lambda: self.start_button_callback(
                bot_key_frame=bot_key_frame,
                bot_list_frame=bot_list_frame
            ),
            fg_color=green_color,
            hover_color=green_color
        )
        self.start_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # STOP BUTTON
        red_color = "#b71c1c"
        self.stop_button = customtkinter.CTkButton(
            self,
            text="Stop",
            command=self.stop_button_callback,
            fg_color=red_color,
            hover_color=red_color
        )
        self.stop_button.grid(row=1, padx=10, pady=10, sticky="ew")

    # START BUTTON CALLBACK
    def start_button_callback(self, bot_key_frame, bot_list_frame):
        """calls tcp server to engage the correct bot"""
        # bot key information
        bot_key = bot_key_frame.bot_key_entry.get()
        # selected bot
        name = "".join(bot_list_frame.get())

        # send selected bot and key to server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("localhost", 3363))
            st = str(name + "/" + bot_key)
            byt = st.encode()
            sock.send(byt)
            sock.close()

    # STOP BUTTON CALLBACK
    def stop_button_callback(self):
        """terminates the system completely"""
        # self destruct app
        sys.exit(1)
