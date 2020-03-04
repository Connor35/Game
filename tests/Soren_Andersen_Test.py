import nose
import unittest
import Game.items
import Game.exits
import Game.inventory
import Game.mobiles
import Game.rooms
import Game.map
import Game.engine

def setup():
    test_inv = Game.inventory.Inventory()
    test_map = Game.map.Map()
    test_map.setup()
    test_player = Game.mobiles.Mobile(test_inv, test_map.all_rooms['tube_room'])
    test_engine = Game.engine.Engine(test_map, test_player)
    return()



def user_input():
    engine = setup()



    user_string1 = ["word", "giant", "  ", "-1", " ", "_"]


    user_string2 = " "
    user_string3 = ["zzz", " "]
    user_string4 = ["wn", "norwest"]
    user_string5 = ["north", "south", "IWantToGoSouth", "West", "east"]
    engine.simulate_play(user_string1)
    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(user_string2)
    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(user_string3)
    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(user_string4)
    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(user_string5)
    assert_equal(engine.player.location.label, "tube_room")




def multiwords():
    multi_keywords = ["move east", "west", "look", "take", "unlock", "south"]
    multi_keywords1 = ["move east north look", "take", "unlock", "south"]
    multi_keywords2 = ["move east", "look take", "unlock south"]
    multi_keywords3 = ["move_east", "north look", "take", "unlock south"]
    multi_keywords4 = ["hair hair est left move"]

    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(multi_keywords2)
    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(multi_keywords3)
    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(multi_keywords4)
    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(multi_keywords)
    assert_equal(engine.player.location.label, "tube_room")
    engine.simulate_play(multi_keywords1)
    assert_equal(engine.player.location.label, "tube_room")






