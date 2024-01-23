"""frame for the bot key extending CTkFrame"""
import customtkinter

class BotKeyFrame(customtkinter.CTkFrame):
    """responsible for bot key interactions"""
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=4)
        bot_key_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="🔑 paste gold membership key",
            state="disabled"
        )
        bot_key_entry.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew")
