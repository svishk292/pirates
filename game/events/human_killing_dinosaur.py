from game import event
import random
from game.combat import Combat
from game.combat import Macaque
from game.display import announce
import game.config as config

class HumanKillingDinosaur (event.Event):

    def __init__ (self):
        self.name = " dinosaur attack"

    def process (self, world):
        result = {}
        result["message"] = "the terasaurus are defeated! ...Those look pretty tasty to eat!"
        monsters = []
        n_appearing = random.randrange(4,8)
        n = 1
        while n <= n_appearing:
            monsters.append(Macaque("Human-Killing Dinosaur "+str(n)))
            n += 1
        announce ("The crew is attacked by a troop of human kill dinosaur!")
        Combat(monsters).combat()
        if random.randrange(2) == 0:
            result["newevents"] = [ self ]
        else:
            result["newevents"] = [ ]
        config.the_player.ship.food += n_appearing*2
        
        return result