from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Princess (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "Princess appearing"
        self.Princesss = 1
        self.verbs['chase'] = self
        self.verbs['feed'] = self
        self.verbs['fun'] = self
        self.verbs['talk'] = self
        self.verbs['kill'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
             self.result["message"] = "the Princess fly off."
             self.go = True
        
        elif (verb == "kill"):
             self. result ["newevents"]. append (Princess())
             self. result ["message"] = "You killed the Princesss. Now it's your dinner for today."
             amount = random. randint (70, 80)
             ship_utility = config.the_player.ship
             ship_utility.food = ship_utility.food + amount
             self.go = True

        elif (verb == "feed"):
            self.Princesss = self.Princesss + 1
            self.result["newevents"].append (Princess())
            self.result["message"] = "the Princess is happy"
            config.the_player.ship.food = config.the_player.ship.food - config.the_player.ship.food * 1/2
            self.go = True
        elif (verb == "fun"):
            print ("the Princess will sleep with you for one night")
            self.go = False
        elif (verb == "talk"):
            print ("the Princess is fliping her middle finger to you.")
            self.go = False
        else:
            print ("it seems the only options here are to feed or fun or talk or kill or chase")
            self.go = False



    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = []
        self.result["message"] = "default message"

        while (self.go == False):
            print (str (self.Princesss) + " Princesss has appeared what do you want to do? Please tell naa: ")
            Player.get_interaction ([self])

        return self.result
