from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Fish (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "Fish visitor"
        self.Fishs = 1
        self.verbs['chase'] = self
        self.verbs['feed'] = self
        self.verbs['help'] = self
        self.verbs['kill'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
             self.result["message"] = "the Fishs looks so beautiful iin the ocean."
             self.go = True
        
        elif (verb == "kill"):
             self. result ["newevents"]. append (Fish())
             self. result ["message"] = "You have caught the Fish. Now it's your dinner for today"
             amount = random. randint (16, 19)
             ship_utility = config.the_player.ship
             ship_utility.food = ship_utility.food + amount
             self.go = True

        elif (verb == "feed"):
            self.Fishs = self.Fishs + 3
            self.result["newevents"].append (Fish())
            self.result["message"] = "You have served fish food, the Fishs are happy"
            self.go = True
        elif (verb == "help"):
            print ("the Fishs will float with you until you feed them or chase them off")
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
            print (str (self.Fishs) + " Fishs have came into view what do you want to do? Please tell naa: ")
            Player.get_interaction ([self])

        return self.result
