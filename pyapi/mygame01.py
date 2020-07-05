#!/usr/bin/env python3

def showInstructions():
    print('''
    RPG Game
    =======
    Commands:
        go[direction]
        get[item]
    ''')
def showStatus():
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory: ' + str(inventory))
    print('\n###############')
    
    print('You see :')
    for option in rooms[currentRoom]:
        if option == 'item':
            print(' \''+rooms[currentRoom]['item']+'\'')
    
    print('\nYou can go to :')
    for option in rooms[currentRoom]:
        if option == 'south' or option == 'east' or option == 'north' or option == 'west':
            print(' \''+ option+'\'')

    # if "item" in rooms[currentRoom]:
    #    print('You see a '+ rooms[currentRoom]['item'])
    print('---------------------------')

#an inventory, whihc is initially empty
inventory = []

#a dictionary linking a room to other room
rooms = {
        'Hall' : {
            'south' : 'Kitchen',
            'east' : 'Dining Room',
            'item' : 'key'
            },
        'Kitchen':{
            'north' : 'Hall',
            'item' : 'monster'
            },
        'Dining Room':{
            'west': 'Hall',
            'south' : 'Garden',
            'item' : 'portion'
            },
        'Garden':{
            'north' : 'Dining Room'
            }
        }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever - game loop
while True:
    showStatus()

   # for option in rooms[currentRoom]:
   #     if option != 'item'
   #         print(option)

    move = ''
    while move == '':

        #Take input
        move = input('>')
    
    # split allows an items to have a space on them
    # get golden ley is returned ["get","golden key"]
    move = move.lower().split(" ", 1)

    # Say you type 'go south'
    # -> 'go' is stored in move[0] and 'south' is stored in move[1] 
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')
    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')

            del rooms[currentRoom]['item']
        else:
            print('Can\'t get '+ move[1]+'!')

## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER')
        break;

## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'portion' in inventory:
        print('You escaped the house with the ultra rare key and magic portion... YOU WIN!')
        break

