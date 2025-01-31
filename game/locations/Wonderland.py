
from game import location
from game import config
from game.display import announce
from game.events import *
from game.items import Ironsword
from game.items import Guntrail

class Wonderland (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "Wonderland"
        self.symbol = 'W'
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.locations["rides"] = Rides(self)
        self.locations["gold"] = Gold(self)
        self.locations["tokyo"] = Tokyo(self)
        self.locations["india"] = India(self)

    def enter (self, ship):
        print ("Arrived at the entrance gate of the Wonderland Amusement park.")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Beach_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "beach"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        
        self.event_chance = 50
        self.events.append (seagull.Seagull())
#         self.events.append(riding_pirates.RidingPirates())

    def enter (self):     #go ashore
        announce ("Arrive at the beach port. Your ship is at an anchor in the bay of the southern part of ocean.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["rides"]
            announce ("You walk all the way around the Wonderland to see the rides inside it from the gate. You see few people riding the roller coster.")
        elif (verb == "east"):
            pass
        elif (verb == "west"):
            pass


class Rides (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "rides"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        # Include a couple of items and the ability to pick them up, for demo purposes
        self.verbs['take'] = self
        self.item_in_tree = Ironsword()
        self.item_in_clothes = Guntrail()

        self.event_chance = 50
        self.events.append(human_killing_dinosaur.HumanKillingDinosaur())
        self.events.append(riding_pirates.RidingPirates())

    def enter (self):
        rideable = False
        for e in self.events:
            if isinstance(e, human_killing_dinosaur.HumanKillingDinosaur):
                rideable = True
        #The description has a base description, followed by variable components.
        description = "You walk into the Wonderland amusement park to give a check upon the rides."
        if rideable == False:
             description = description + " Nothing around here looks very interesting to ride."
        
        #Add a couple items as a demo. This is kinda awkward but students might want to complicated things.
        '''if self.item_in_tree != None:
            description = description + " You see a " + self.item_in_tree.name + " stuck in a ride."
        if self.item_in_clothes != None:
            description = description + " You see a " + self.item_in_clothes.name + " in a pile of shredded iron metal rods of rides on the amusement park floor."
        announce (description)'''
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["beach"] 
            announce ("We are returning back to beach")
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["gold"]
            announce ("You see the piramid from far....you are approaching towards it.")
        #Handle taking items. Demo both "take Ironsword" and "take all"
        '''if verb == "take":
            if self.item_in_tree == None and self.item_in_clothes == None:
                announce ("You don't see anything to take.")
            elif len(cmd_list) > 1:
                at_least_one = False #Track if you pick up an item, print message if not.
                item = self.item_in_tree
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You take the "+item.name+" from the tree.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_tree = None
                    config.the_player.go = True
                    at_least_one = True
                item = self.item_in_clothes
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You pick up the "+item.name+" out of the pile of clothes. ...It looks like someone was eaten here.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_clothes = None
                    config.the_player.go = True
                    at_least_one = True
                if at_least_one == False:
                    announce ("You don't see one of those around.")
'''
        
####################################################
        
class Gold (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Gold"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        # Include a couple of items and the ability to pick them up, for demo purposes
        self.verbs['take'] = self
        self.item_in_tree = Ironsword()
        self.item_in_clothes = Guntrail()

        self.event_chance = 100
        self.events.append(mummyattack.Mummyattack())
#         self.events.append(human_killing_dinosaur.HumanKillingDinosaur())
#         self.events.append(snake.Snake())
#         self.events.append(princess.Princess())


    def enter (self):
        rideable = False
        for e in self.events:
            if isinstance(e, human_killing_dinosaur.HumanKillingDinosaur):
                rideable = True
        #The description has a base description, followed by variable components.
        description = "You walk in the piramid."
        if rideable == False:
             description = description + " something looks off here. Giving some weird vibes"
        
        #Add a couple items as a demo. This is kinda awkward but students might want to complicated things.
        '''if self.item_in_tree != None:
            description = description + " You see a " + self.item_in_tree.name + " stuck in this piramid."
        if self.item_in_clothes != None:
            description = description + " You see a " + self.item_in_clothes.name + " in a pile of shredded bodies on the floor."
        announce (description)'''
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["rides"]
        elif (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["beach"]
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["tokyo"]
            announce ("We see the some beautiful sturcture representing tokyo drift.")

            
            
        #Handle taking items. Demo both "take Ironsword" and "take all"
        '''if verb == "take":
            if self.item_in_tree == None and self.item_in_clothes == None:
                announce ("You don't see anything to take.")
            elif len(cmd_list) > 1:
                at_least_one = False #Track if you pick up an item, print message if not.
                item = self.item_in_tree
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You take the "+item.name+" from the tree.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_tree = None
                    config.the_player.go = True
                    at_least_one = True
                item = self.item_in_clothes
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You pick up the "+item.name+" out of the pile of clothes. ...It looks like someone was eaten here.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_clothes = None
                    config.the_player.go = True
                    at_least_one = True
                if at_least_one == False:
                    announce ("You don't see one of those around.")
'''
        
        
###########################################################################################################################
        
class Tokyo (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "India"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        # Include a couple of items and the ability to pick them up, for demo purposes
        self.verbs['take'] = self
        self.item_in_tree = Ironsword()
        self.item_in_clothes = Guntrail()

        self.event_chance = 100
#         self.events.append(disneyland.Disneyland())
#         self.events.append(disneyland.Disneyland())
        #self.events.append(human_killing_dinosaur.HumanKillingDinosaur())
#         self.events.append(mummyattack.Mummyattack())
        self.events.append(princess.Princess())
        self.events.append(snake.Snake())


    def enter (self):
        rideable = False
        for e in self.events:
            if isinstance(e, human_killing_dinosaur.HumanKillingDinosaur):
                rideable = True
        #The description has a base description, followed by variable components.
        description = "You walk into tokyo drift to see what in there."
        if rideable == False:
             description = description + " Nothing around here? huh hello!!! Is someone here."
        
        #Add a couple items as a demo. This is kinda awkward but students might want to complicated things.
        '''if self.item_in_tree != None:
            description = description + " You see a " + self.item_in_tree.name + " stuck in the room."
        if self.item_in_clothes != None:
            description = description + " You see a " + self.item_in_clothes.name + " in a smoke layered on the floor."
        announce (description)'''
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["gold"]
        elif (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["india"]
            announce ("This is the market of baniya(trade) they are hypnotised to snatch the money they have.")
        #Handle taking items. Demo both "take Ironsword" and "take all"
        '''if verb == "take":
            if self.item_in_tree == None and self.item_in_clothes == None:
                announce ("You don't see anything to take.")
            elif len(cmd_list) > 1:
                at_least_one = False #Track if you pick up an item, print message if not.
                item = self.item_in_tree
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You take the "+item.name+" from the tree.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_tree = None
                    config.the_player.go = True
                    at_least_one = True
                item = self.item_in_clothes
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You pick up the "+item.name+" out of the pile of clothes. ...It looks like someone was eaten here.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_clothes = None
                    config.the_player.go = True
                    at_least_one = True
                if at_least_one == False:
                    announce ("You don't see one of those around.")
'''
        
################################################################################################################################
        
        
class India (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "india"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        # Include a couple of items and the ability to pick them up, for demo purposes
        self.verbs['take'] = self
        self.item_in_tree = Ironsword()
        self.item_in_clothes = Guntrail()

        self.event_chance = 100
        self.events.append(baniya.Baniya())
#         self.events.append(human_killing_dinosaur.HumanKillingDinosaur())
#         self.events.append(riding_pirates.RidingPirates())

    def enter (self):
        rideable = False
        for e in self.events:
            if isinstance(e, human_killing_dinosaur.HumanKillingDinosaur):
                rideable = True
        #The description has a base description, followed by variable components.
        description = "You walk into the rides in the Wonderland amusement park to give a check upon it."
        if rideable == False:
             description = description + " Nothing around here looks very rideable."
        
        #Add a couple items as a demo. This is kinda awkward but students might want to complicated things.
        '''if self.item_in_tree != None:
            description = description + " You see a " + self.item_in_tree.name + " stuck in a ride."
        if self.item_in_clothes != None:
            description = description + " You see a " + self.item_in_clothes.name + " in a pile of shredded iron metal rods of rides on the amusement park floor."
        announce (description)'''
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["tokyo"]
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["rides"]
            announce ("back to amusement park")
        #Handle taking items. Demo both "take Ironsword" and "take all"
        '''if verb == "take":
            if self.item_in_tree == None and self.item_in_clothes == None:
                announce ("You don't see anything to take.")
            elif len(cmd_list) > 1:
                at_least_one = False #Track if you pick up an item, print message if not.
                item = self.item_in_tree
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You take the "+item.name+" from the tree.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_tree = None
                    config.the_player.go = True
                    at_least_one = True
                item = self.item_in_clothes
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You pick up the "+item.name+" out of the pile of clothes. ...It looks like someone was eaten here.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_clothes = None
                    config.the_player.go = True
                    at_least_one = True
                if at_least_one == False:
                    announce ("You don't see one of those around.")
'''
