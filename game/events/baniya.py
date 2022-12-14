from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Baniya (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "You are in the market and baniya is appearing in front of you."
        self.Princesss = 1
        self.verbs['chase'] = self
        self.verbs['feed'] = self
        self.verbs['fun'] = self
        self.verbs['talk'] = self
        self.verbs['kill'] = self
        self.verbs['buy'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
             self.result["message"] = "The baniya disappearded in the rush of market"
             self.go = True
        
        elif (verb == "kill"):
             self. result ["newevents"]. append (Princess())
             self. result ["message"] = "You killed the baniya because he was harassing you."
             amount = random. randint (70, 80)
             ship_utility = config.the_player.ship
#              ship_utility.food = ship_utility.gold - amount
             self.go = True

        elif (verb == "buy"):
            #self.Baniya = self.Baniya + 1
            self.result["newevents"].append (Baniya())
            self.result["message"] = "the Princess is happy. You bought stuff from him but he looted you."
            config.the_player.ship.gold = config.the_player.ship.gold - config.the_player.ship.gold * 1/4
            self.go = True
        elif (verb == "fun"):
            print ("the baniya has came out as gay")
            self.go = False
        elif (verb == "talk"):
            print ("the baniya is ready to do the bargening with you. but he is shouting")
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
            print (str (self.Princesss) + " baniya has appeared. what do you want to do? Please tell naa: ")
            Player.get_interaction ([self])

        return self.result
