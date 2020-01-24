from room import Room
from player import Player
import textwrap as tw

"""
Simple text adventure game, use N, S, E, W, or Q to play the game, can set name by changing the name in quotes on line 47
"""

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

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

# Make a new player object that is currently in the 'outside' room.
my_player = Player("Jesse", room['outside'])
current_room = (switch_room("[N] North [S] South [E] East [W] West [Q]\n"))



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.
print(f"Please enter a valid direction")
#
# If the user enters "q", quit the game.


def switch_room(player_input):
    if player_input == 'n':
        if player.current_room.n_to is None:
            print('\n\n Please enter a valid direction\nYou are currently in')
        else:
            player.current_room = player.current_room.n_to
        elif player_input == 's':
                    if player.current_room.s_to is None:
            print('\n\n Please enter a valid direction\nYou are currently in')
        else:
            player.current_room = player.current_room.s_to
        elif player_input == 'e':
                    if player.current_room.e_to is None:
            print('\n\n Please enter a valid direction\nYou are currently in')
        else:
            player.current_room = player.current_room.s_to
        elif player_input == 'w':
                    if player.current_room.w_to is None:
            print('\n\n Please enter a valid direction\nYou are currently in')
        else:
            player.current_room = player.current_room.s_to
            

player_input = None
while player_input != 'q':
    print ('\n\n' + player.current_room.name + '\n\n' + textwrap.fill(player.current_room.description, 87))