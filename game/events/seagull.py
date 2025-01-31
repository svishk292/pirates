from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Seagull (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "seagull visitor"
        self.seagulls = 1
        self.verbs['chase'] = self
        self.verbs['feed'] = self
        self.verbs['help'] = self
        self.verbs['kill'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
             self.result["message"] = "the seagull fly off."
             self.go = True
        
        elif (verb == "kill"):
             self. result ["newevents"]. append (Seagull())
             self. result ["message"] = "You killed the seagulls. Now it's your dinner for today"
             amount = random. randint (15, 18)
             ship_utility = config.the_player.ship
             ship_utility.food = ship_utility.food + amount
             self.go = True

        elif (verb == "feed"):
            self.seagulls = self.seagulls + 1
            self.result["newevents"].append (Seagull())
            self.result["message"] = "the seagulls are happy"
            self.go = True
        elif (verb == "help"):
            print ("the seagulls will pester you until you feed them or chase them off")
            self.go = False
        else:
            print ("it seems the only options here are to feed or chase or kill")
            self.go = False



    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print (str (self.seagulls) + " seagulls has appeared what do you want to do? Please tell naa: ")
            Player.get_interaction ([self])

        return self.result
