from game import event
import random
from game.combat import Combat
from game.combat import Snakes
from game.display import announce
import game.config as config

class Mummyattack :
    
        
    def __init__ (self):
        self.name = " mummies have attack"

    def process (self, world):
        result = {}
        result["message"] = "mummies has been defeated! ...Those look very scary! \n Your received the gold as your reward."
        monsters = []
        n_appearing = random.randrange(2,5)
        n = 1
        while n <= n_appearing:
            monsters.append(Snakes(" human eating mummies"+str(n)))
            n += 1
        announce ("The crew is attacked by a troop of mummies!")
        Combat(monsters).combat()
        result["newevents"] = [ ]
        config.the_player.ship.gold += n_appearing*2
        
        return result