"""Application Runner"""
import sys
import customtkinter
from osrs_python_bot.src.bots.magic import Magic


class AvailableBotsFrame(customtkinter.CTkFrame): # pylint: disable=too-few-public-methods
    """List the available bots menu."""
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="High Alchemy")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="Nightmare Zone")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")


class App(customtkinter.CTk): # pylint: disable=too-few-public-methods
    """Application Class"""
    def __init__(self):
        super().__init__()

        self.title("osrs-bots")
        self.geometry("400x250")
        self.grid_columnconfigure((0, 1), weight=2)

        # BOTS LIST
        self.checkbox_frame = AvailableBotsFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), columnspan=2)

        # START BUTTON
        self.start_button = customtkinter.CTkButton(
            self, text="start", command=self.start_button_callback,
            fg_color="green", hover_color="green"
        )
        self.start_button.grid(row=2, column=0, padx=20, pady=30, sticky="ew", columnspan=2)

        # STOP BUTTON
        self.stop_button = customtkinter.CTkButton(
            self, text="stop", command=self.stop_button_callback,
            fg_color="red", hover_color="red"
        )
        self.stop_button.grid(row=3, column=0, padx=20, pady=1, sticky="ew", columnspan=2)

    def start_button_callback(self):
        """"Start Button"""
        Magic().high_alchemy()


    def stop_button_callback(self):
        """"Stop Button"""
        sys.exit(0)

app = App()
app.mainloop()
