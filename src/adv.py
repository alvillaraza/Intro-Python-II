# class Room:
#     def __init__(self, name, desc):
#         self.name = name
#         self.desc = desc


# class Player:
#     def __init__(self, name, room):
#         self.name = name
#         self.room = room

from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    #  {
    # 'name' :'Outside Cave Entrance',
    # 'desc': 'North of you, the cave mount beckons'
    # }

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# # Make a new player object that is currently in the 'outside' room.
# currentPlayer = Player(input("what is your name?"), input("what room?"))
me = Player('alexis', room['outside'])
# Write a loop that:
while True:
    # * Prints the current room name
    print(me.name, me.room.name, me.room.desc)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    direction = input('Where would you like to go?')
    print(direction)
#

# If the user enters a cardinal direction, attempt to move to the room there.

    # me.room = me.room.{direction}_to
    if direction == "n":
        me.room = me.room.n_to
        print(me.room.name)

    elif direction == 's':
        me.room = me.room.s_to
        print(me.room.name)

    elif direction == 'e':
        me.room = me.room.e_to
        print(me.room)

    elif direction == 'w':
        me.room = me.room.w_to
        print(me.room.name)

    # elif:
    #     print("You're lost")
    
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    elif direction == 'q':
        print('Game Over')
        break
    
    else:
        print('youre lost')
        
