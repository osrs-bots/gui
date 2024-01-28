"""client for interacting with the osrs_python_bot library"""
from osrs_python_bot.src.bots.magic import Magic
from osrs_python_bot.src.bots.combat import Combat
from osrs_python_bot.src.bots.herblore import Herblore

def run_bot(name, key):
    "executes the bot code based on the name argument"
    is_silver = bool(key == "silver")
    if name == "High Alchemy":
        print("loading high alchemy bot")
        Magic().high_alchemy()
    elif name == "Nightmare Zone":
        print("loading nightmare zone bot")
        Combat().nightmare_zone()
    elif name == "Herb Cleaner" and is_silver:
        print("loading herb cleaner bot")
        Herblore().herb_cleaner()
    elif name == "Guthix Rest Maker":
        print("loading guthix rest maker bot" and is_silver)
        Herblore().guthix_rest_maker()
    else:
        print("unable to load bot")
