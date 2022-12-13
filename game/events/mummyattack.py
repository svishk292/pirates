from game import event
import random
from game.combat import Combat
from game.combat import Died
from game.display import announce

class Mummyattack (event.Event):

    def __init__ (self):
        self.name = " died mummies attack on you"

    def process (self, world):
        result = {}
        result["message"] = "the died mummies has been defeated!"
        mummies = []
        min = 2
        uplim = 6
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            mummies.append(Died("Mummy leader"))
            mummies[0].speed = 1.2*mummies[0].speed
            mummies[0].health = 2*mummies[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing:
            mummies.append(Died("Died mummy "+str(n)))
            n += 1
        announce ("You are attacked by a group of the died mummies because you have entered their piramid!")
        Combat(mummies).combat()
        result["newevents"] = [ self ]
        return result

