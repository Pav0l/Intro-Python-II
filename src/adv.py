from room import Room
from player import Player
from items import Item
import time
import random

# Declare all the rooms

room = {
    'outside':  Room("Cave Entrance",
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

# Create items

items = {
    'sword': Item('Thunderfury, Blessed Blade of the Windseeker', 'Damage', 30, 'melee'),
    'staff': Item('Atiesh, Greatstaff of the Guardian', 'Intellect', 34, 'melee'),
    'mace': Item('Sulfuras, Hand of Ragnaros', 'Fire resistance', 15, 'melee'),
    'axe': Item('Shadowmourne', 'Strength', 24, 'melee'),
    'bow': Item("Thori'dal, the Stars' Fury", 'Agility', 19, 'ranged'),
    'wand': Item('Crimson Shocker', 'Stamina', 10, 'ranged')
}


def add_item_to_room(room):
    success = False
    rand_generator = random.randint(1, 10)
    # give 30% chance for a item drop when entering a room
    if rand_generator < 8:
        # add a random item from items dict to the room
        item_in_room = items[random.choice(list(items))]
        room.items = item_in_room
        print('*****************************************')
        print(f'You found: \n{item_in_room.name} in the {room.name}')
        print(item_in_room)
        print('*****************************************')
        success = True
    else:
        success = False
    return success


def get_item(item, player):
    item_slot = item.slot
    success = False
    # check if player already has an item in this slot
    if player.items[item_slot]:
        print('\nYou already have an item in this slot. You must drop it before picking up another item.\n')
        success = False
    else:
        player.items[item_slot] = item
        success = True
    return success


def drop_item(item_slot, player):
    print(f'\nYou have droped {player.items[item_slot].name}')
    player.items[item_slot] = None


def get_help():
    return print('You will move througout the game with specific keys:\n  n - for North\n  s - for South\n  e - for East\n  w - for West\n  h - for Help\n  q - to Quit the game')


def move_direction(where):
    dir_name = ''
    if where == 'n':
        dir_name = 'North'
    elif where == 's':
        dir_name = 'South'
    elif where == 'w':
        dir_name = 'West'
    elif where == 'e':
        dir_name = 'East'

    print(f'\nYou start walking {dir_name}')
    for i in [1, 2, 3]:
        print('...walking')
        time.sleep(0.3)


# Make a new player object that is currently in the 'outside' room.
new_player = Player('Joe', room['outside'])

# initial location
directions = ''

print(
    f'\n### WELCOME {new_player.name.upper()} TO THE WORLD OF ADVENTURES! ### ')
get_help()
print('\n LET THE ADVENTURE BEGIN! \n')
while directions != 'q':
    print(f'\nYou move to {new_player.current_room.name}')
    print(new_player.current_room.description + '\n')

    result = add_item_to_room(new_player.current_room)
    # Ask if player wants to pick up newly found item
    if result:
        pick_up = input('Would you like to pick it up [y/n]? ').lower()
        # Check if he has an empty slot
        if pick_up == 'y':
            get_result = get_item(new_player.current_room.items, new_player)

            if not get_result:
                wanna_drop_item = input(
                    f'Do you want to drop it [y/n]? ').lower()

                if wanna_drop_item == 'y':
                    # drop current item in a slot
                    drop_item(new_player.current_room.items.slot, new_player)
                    # and add new item to that slot
                    get_item(new_player.current_room.items, new_player)
                    print(
                        f"\nYou've picked up {new_player.current_room.items.name}")
                elif wanna_drop_item == 'n':
                    print('You kept your current item')
                else:
                    print(
                        'Oh no, you accidentaly destroyed the item by giving bad input :(')
            else:
                print(
                    f"\nYou've picked up {new_player.current_room.items.name}")
        elif pick_up == 'n':
            continue
        else:
            print(
                '\nOh no, you accidentaly destroyed the item by giving bad input :(\n')

    directions = input(
        'What is your next move? ').lower()
    try:
        if directions == 'n':
            if new_player.current_room.n_to:
                new_player.current_room = new_player.current_room.n_to
                move_direction(directions)
                directions == ''
            else:
                print('There is nothing here, try another direction.')
        elif directions == 's':
            if new_player.current_room.s_to:
                new_player.current_room = new_player.current_room.s_to
                move_direction(directions)
                directions == ''
            else:
                print('There is nothing here, try another direction.')
        elif directions == 'w':
            if new_player.current_room.w_to:
                new_player.current_room = new_player.current_room.w_to
                move_direction(directions)
                directions == ''
            else:
                print('There is nothing here, try another direction.')
        elif directions == 'e':
            if new_player.current_room.e_to:
                new_player.current_room = new_player.current_room.e_to
                move_direction(directions)
                directions == ''
            else:
                print('There is nothing here, try another direction.')
        elif directions == 'h':
            get_help()
        elif directions == 'q':
            print('\nThanks for playing!\n')
            break
        else:
            print('*** Wrong input ***')
            print('You must choose correct direction n/w/e/s or q to quit')

    except:
        print('Bad input')
