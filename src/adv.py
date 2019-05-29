from room import Room
from player import Player
import time

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
new_player = Player('Joe', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# initial location
directions = ''

while directions != 'q':
    print(f'\nYou are in the {new_player.current_room.name}')
    print(new_player.current_room.description + '\n')

    directions = input(
        'Where would you like to go next? n/w/e/s or q to quit: ').lower()
    try:

        if directions == 'n':
            if new_player.current_room.n_to:
                new_player.current_room = new_player.current_room.n_to
                print('\n===== You start moving north =====')
                time.sleep(1)
                directions == ''
            else:
                print('There is nothing here, try another direction.')
        elif directions == 's':
            if new_player.current_room.s_to:
                new_player.current_room = new_player.current_room.s_to
                print('\n===== You start moving south =====')
                time.sleep(1)
                directions == ''
            else:
                print('There is nothing here, try another direction.')
        elif directions == 'w':
            if new_player.current_room.w_to:
                new_player.current_room = new_player.current_room.w_to
                print('\n===== You start moving west =====')
                time.sleep(1)
                directions == ''
            else:
                print('There is nothing here, try another direction.')
        elif directions == 'e':
            if new_player.current_room.e_to:
                new_player.current_room = new_player.current_room.e_to
                print('\n===== You start moving east =====')
                time.sleep(1)
                directions == ''
            else:
                print('There is nothing here, try another direction.')
        elif directions == 'q':
            print('Thanks for playing! Hope you had fun\n')
            break
        else:
            print('*** Wrong input ***')
            print('You must choose correct direction n/w/e/s or q to quit')

    except:
        print('Bad input')
