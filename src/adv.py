from room import Room
from player import Player
from item import RoomItem
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'backpack'),
    #  {
    # 'name' :'Outside Cave Entrance',
    # 'desc': 'North of you, the cave mount beckons'
    # }

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'shovel'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'key'),

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

item = {
  'backpack': RoomItem('Backpack', 'used for storing items'),
  'shovel': RoomItem('Shovel', 'used for digging'),
  'key': RoomItem('Key', 'used for opening locks'),
  # 'backpack': {
  #   name: 'Backpack',
  #   desc: 'used for storing items'
  # }
}

#
# Main
#

# # Make a new player object that is currently in the 'outside' room.
me = Player('Alexis', room['outside'])
# Write a loop that:
while True:
    # * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    print(f"You are in the {me.current_room.name} You see the following item: {me.current_room.items[0].name}")
    for line in textwrap.wrap(me.current_room.desc, 50):
        print(line)

# * Waits for user input and decides what to do.
    print(me.current_room.items[0].name)
    action = input("What would you like to do? (take[item], drop[item])")
    if action == f"take {me.current_room.items[0].name}":
        # if {me.current_room.item == None}:
        me.get_item(me.current_room.items[0])
        me.current_room.remove_item(me.current_room.items[0])
        print(f"{me.current_room.name} contains the following items: {me.current_room.items[0].name}")

    # if action == f"drop {me.has_item.name}":
    #     me.current_room.add_item(me.has_item)
    #     me.drop_item()
        #else "the room is empty"
    # if action == f"drop {me.current_room.item.name}":

    
    #### if action == "drop {}"####

    direction = input('Where would you like to go? (n/e/s/w)')
    print(f"You went {direction}.")



# If the user enters a cardinal direction, attempt to move to the room there.

    if direction == "n":
        me.current_room = me.current_room.n_to
        print(me.current_room.name)

    elif direction == 's':
        me.current_room = me.current_room.s_to
        print(me.current_room.name)

    elif direction == 'e':
        me.current_room = me.current_room.e_to
        print(me.current_room)

    elif direction == 'w':
        me.current_room = me.current_room.w_to
        print(me.current_room.name)
    
    elif direction == 'i' or direction == 'inventory':
        print(me.has_item.name, me.current_room.items[0].name)

  
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    elif direction == 'q':
        print('Game Over')
        break
    
    else:
        print('youre lost')
        
