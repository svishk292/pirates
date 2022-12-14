
from game import event
import random
import game.config as config

class Disneyland (event.Event):

    def __init__ (self):
        self.name = " You are having a beautiful day with the princess"

    def process (self, world):
        # choose a lucky crew member
        
        c = random.choice(config.the_player.get_pirates())
        msg = c.get_name() + " is having a fun day"
        c.lucky = True
        result = {}
        result["message"] = msg
        result["newevents"] = [ self ]
        return result