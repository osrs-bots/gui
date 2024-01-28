"""frame for the bot key extending CTkFrame"""
import customtkinter

class BotKeyFrame(customtkinter.CTkFrame):
    """responsible for bot key input"""
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=4)

        bot_key_entry_label = customtkinter.CTkLabel(
            self,
            text="Bot Key"
        )

        bot_key_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="~ paste gold key here ~ !"
        )
        self.bot_key_entry = bot_key_entry

        bot_key_entry_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="w")
        bot_key_entry.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="ew")
