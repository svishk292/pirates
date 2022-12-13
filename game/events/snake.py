from game import event
import random
from game.combat import Combat
from game.combat import Snakes
from game.display import announce
import game.config as config

class Snake :
    
        
    def __init__ (self):
        self.name = " snake bites"

    def process (self, world):
        result = {}
        result["message"] = "snakes has been defeated! ...Those look pretty tasty and yummy! \n Your received the gold as your reward."
        monsters = []
        n_appearing = random.randrange(2,5)
        n = 1
        while n <= n_appearing:
            monsters.append(Snakes(" skin eating snakes"+str(n)))
            n += 1
        announce ("The crew is attacked by a troop of snakes!")
        Combat(monsters).combat()
        result["newevents"] = [ ]
        config.the_player.ship.food += n_appearing*2
        config.the_player.ship.gold += n_appearing*2
        
        return result

        '''if random.randrange(2) == 0:
            result["newevents"] = [ self ]'''
        
        