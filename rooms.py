
rooms_list = ''

"""

Controls for the game is n for north, s for south, e for east and finally - w for west.
Numbers in dictionary is corrensponding to the room which you are navigating to.

"""
#This gets the zip-lock Environment
#print(rooms_list[1]['environment'])

rooms_list = [
    {
        'number': 0,
        'name': 'The Tent',
        'environment': 'green tent sheets(walls), a red sleeping bag, a hat with a feather',
        'north': 2,
        'south': 3,
        'east': 4,
        'west': 5,
    },
    {
        'number': 1,
        'name': 'The Tent Entrance',
        'environment': 'zip-lock',
        'north': 3,
        'south': 4,
        'east': 1,
        'west': 2,

    },
    {
        'number': 2,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 3,
        'south': 2,
        'east': 2,
        'west': 1,
    },
]