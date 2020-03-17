#Adding necessary include files used map.py
import items
import exits
import rooms

class Map(object): 
    def setup(self):
        # This will populate the map with the rooms, exits, and items in the different rooms
        self.all_items = items.populate() # Items from csv to the rooms
        self.all_exits = exits.populate() # Paths through the map
        self.all_rooms = rooms.populate() # Different rooms in the game
        
        # This will iterate through labels and rooms to adds the items and connections
        for label, room in self.all_rooms.iteritems():
            room.add_items(self.all_items) # Adds items where they should be
            room.add_exits(self.all_exits) # Adds room connections where they should be
