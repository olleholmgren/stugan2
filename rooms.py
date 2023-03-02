
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
        'north': ,
        'south': ,
        'east': ,
        'west': ,
    },
    {
        'number': 1,
        'name': 'The Tent Entrance',
        'environment': 'zip-lock',
        'north': 0,
        'south': 10,
        'east': 8,
        'west': 2,

    },
    {
        'number': 2,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 3,
        'south': 11,
        'east': 1,
        'west': 13,
    },
    {
        'number': 3,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 4,
        'south': 2,
        'east': null,
        'west': 14,
    },
    {
        'number': 4,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': null,
        'south': 3,
        'east': 5,
        'west': 15,
    },
    {
        'number': 5,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': null,
        'south': null,
        'east': 6,
        'west': 4,
    },
    {
        'number': 6,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': null,
        'south': 7,
        'east': null,
        'west': 5,
    },
    {
        'number': 7,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 6,
        'south': 8,
        'east': null,
        'west': null,
    },
    {
        'number': 8,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 7,
        'south': 9,
        'east': null,
        'west': 1,
    },
    {
        'number': 9,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 8,
        'south': null,
        'east': null,
        'west': 10,
    },
    {
        'number': 10,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 1,
        'south': null,
        'east': 9,
        'west': 11,
    },
    {
        'number': 11,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 2,
        'south': null,
        'east': 10,
        'west': 12,
    },
    {
        'number': 12,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 13,
        'south': null,
        'east': 11,
        'west': null,
    },
    {
        'number': 13,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 14,
        'south': 12,
        'east': 2,
        'west': null,
    },
    {
        'number': 14,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': 15,
        'south': 13,
        'east': 3,
        'west': null,
    },
    {
        'number': 15,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'north': null,
        'south': 14,
        'east': 4,
        'west': null,
    },
]