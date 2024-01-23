"""client for interacting with the osrs_python_bot library"""
from osrs_python_bot.src.bots.magic import Magic
from osrs_python_bot.src.bots.combat import Combat

def run_bot(name):
    "executes the bot code based on the name argument"
    if name == "High Alchemy":
        print("Loading High Alchemy Bot")
        Magic().high_alchemy()
    elif name == "Nightmare Zone":
        print("Loading Nightmare Zone Bot")
        Combat().nightmare_zone()
