"""bot list frame extending CTkScrollableFrame"""
import customtkinter

class BotListFrame(customtkinter.CTkScrollableFrame):
    """list checkboxes for the available bots"""
    def __init__(self, master, title):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = ["High Alchemy", "Nightmare Zone",]
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(
                self,
                text=value,
                command=self.select_bot_callback(value=value)
            )
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        """get currently selected bot from the bot_list_frame"""
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

    def select_bot_callback(self, value):
        """unselects previously selected bot and replaces with new selection"""
        def custom_handler():
            for checkbox in self.checkboxes:
                if checkbox.cget("text") != value:
                    checkbox.deselect()
                else:
                    checkbox.select(0)
        return custom_handler
