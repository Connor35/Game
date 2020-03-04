from nose.tools import *
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
    return(test_engine)


def test_win_case1():
    engine = setup()

    # this exact sequence should win the game
    win_case = [
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        'take keycard',
        'go south',
        'go east',
        'go south',
        'take parka',
        'go north',
        'go east',
        'go south',
        'look body',
        'cut key',
        'take key',
        'go north',
        'go west',
        'go north',
        'look fridge',
        'take syringe',
        'inject self',
        'go south',
        'go west',
        'go west',
        'go south',
        'unlock cylinder',
        'take rod',
        'go north',
        'go east',
        'go east',
        'go east',
        'go south',
        'fix snowmobile'
    ]

    # simulate the play
    engine.simulate_play(win_case)

    # see if the player is in the correct room and that they have won the game
    assert_equal(engine.player.location.label, 'garage')
    assert_equal(engine.player.victory, True)


def test_win_case2():
    engine = setup()

    # this is a different sequence needed to win the game
    win_case = [
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        'take keycard',
        'go south',
        'go east',
        'go south',
        'take parka',
        'go north',
        'go east',
        'go south',
        'look body',
        'cut key',
        'take key',
        'go north',
        'go west',
        'go north',
        'look fridge',
        'take syringe',
        'inject self',
        'go south',
        'go west',
        'go west',
        'go south',
        'unlock cylinder',
        'take rod',
        'go north',
        'go east',
        'go east',
        'go west',              # a few extra, unnecessary moves
        'go east',
        'go east',
        'go south',
        'fix snowmobile'
    ]

    # simulate the play
    engine.simulate_play(win_case)

    # see if the player is in the correct room and that they have won the game
    assert_equal(engine.player.location.label, 'garage')
    assert_equal(engine.player.victory, True)


def test_win_case3():
    engine = setup()

    # this is a third sequence needed to win the game
    win_case = [
        'go west',              # different start move
        'go east',
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        'take keycard',
        'go south',
        'go east',
        'go south',
        'take parka',
        'go north',
        'go east',
        'go south',
        'look body',
        'cut key',
        'take key',
        'go north',
        'go west',
        'go north',
        'look fridge',
        'take syringe',
        'go south',
        'go west',
        'go west',
        'inject self',  # inject self at different portion of game
        'go south',
        'unlock cylinder',
        'take rod',
        'go north',
        'go east',
        'go east',
        'go east',
        'go south',
        'fix snowmobile'
    ]

    # simulate the play
    engine.simulate_play(win_case)

    # see if the player has won the game
    assert_equal(engine.player.victory, True)


def test_non_win_case1():
    engine = setup()

    # this is a third sequence needed to win the game
    win_case = [
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        'take keycard',
        'go south',
        'go east',
        'go south',
        'take parka',
        'go north',
        'go east',
        'go south',
        'look body',
        'cut key',
        'take key',
        'go north',
        'go west',
        'go north',
        'look fridge',
        'take syringe',
        'go south',
        'go west',
        'go west',
        'go south',
        'inject self',  # inject self at different portion of game
        'unlock cylinder',
        'take rod',
        'go north',
        'go east',
        'go east',
        'go east',
        'go south',
        'fix snowmobile'
    ]

    # simulate the play
    engine.simulate_play(win_case)

    # see if the player has won the game
    assert_equal(engine.player.victory, True)


def test_non_win_case2():
    engine = setup()

    # this is a third sequence needed to win the game
    win_case = [
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        'take keycard',
        'go south',
        'go east',
        'go south',
        'take parka',
        'go north',
        'go east',
        'go south',
        'look body',
        'cut key',
        'take key',
        'go north',
        'go west',
        'go north',
        # 'look fridge',        # try to complete the game without getting the syringe
        # 'take syringe',
        'go south',
        'go west',
        'go west',
        'go south',
        'unlock cylinder',
        'take rod',
        'go north',
        'go east',
        'go east',
        'go east',
        'go south',
        'fix snowmobile'
    ]

    # simulate the play
    engine.simulate_play(win_case)

    # see if the player has won the game
    assert_equal(engine.player.victory, True)




#################################
#   PLAYER INTERACTION  TESTING #
#################################

def test_player_interaction1():
    engine = setup()

    try_door_no_key = [
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        # 'take keycard', # remove this line to attempt opening the locked door without a key
        'go south',
        'go east',
        'go south',
        'take parka',
        'go north',
        'go east'
    ]

    engine.simulate_play(try_door_no_key)

    # this tests to make sure that the player could not open the door ...
    # ... without the key
    assert_equal(engine.player.location.label, 'central_hallway_east')
    assert_equal(engine.player.victory, False)

    # give the player the key and try again
    engine.player.inventory.add(engine.map.all_items['keycard']);

    try_door_with_key = [
        'go east'
    ]

    engine.simulate_play(try_door_with_key)

    assert_equal(engine.player.location.label, 'outside')
    assert_equal(engine.player.victory, False)


def test_player_interaction2():
    engine = setup()

    obtain_parka = [
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        'take keycard',
        'go south',
        'go east',
        'go south',
        'take parka'
    ]

    engine.simulate_play(obtain_parka)

    # test if the player was able to obtain the parka
    assert_equal(engine.player.inventory.has('parka'), True)

def test_player_interaction3():
    engine = setup()

    obtain_syringe = [
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        'take keycard',
        'go south',
        'go east',
        'go south',
        'take parka',
        'go north',
        'go east',
        'go south',
        'look body',
        'cut key',
        'take key',
        'go north',
        'go west',
        'go north',
        'look fridge',
        'take syringe'
    ]

    engine.simulate_play(obtain_syringe)

    # test if the player was able to obtain the parka
    assert_equal(engine.player.inventory.has('syringe'), True)


def test_player_interaction4():
    engine = setup()

    obtain_rod = [
        'take scalpel',
        'go west',
        'go north',
        'go north',
        'look corpse',
        'take keycard',
        'go south',
        'go east',
        'go south',
        'take parka',
        'go north',
        'go east',
        'go south',
        'look body',
        'cut key',
        'take key',
        'go north',
        'go west',
        'go north',
        'look fridge',
        'take syringe',
        'inject self',
        'go south',
        'go west',
        'go west',
        'go south',
        'unlock cylinder',
        'take rod'
    ]

    engine.simulate_play(obtain_rod)

    # test if the player was able to obtain the parka
    assert_equal(engine.player.inventory.has('rod'), True)


def test_player_interaction5():
    engine = setup()

    obtain_scalpel = [
        'take scalpel'
    ]

    engine.simulate_play(obtain_scalpel)

    # test if the player was able to obtain the parka
    assert_equal(engine.player.inventory.has('scalpel'), True)
