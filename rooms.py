
rooms_list = ''
null = ''

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
        'step outside': 1,
    },
    {
        'number': 1,
        'name': 'The Tent Entrance',
        'environment': 'You are standing outside your tent',
        'n': 0,
        's': 10,
        'e': 8,
        'w': 2,

    },
    {
        'number': 2,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 3,
        's': 11,
        'e': 1,
        'w': 13,
    },
    {
        'number': 3,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 4,
        's': 2,
        'e': null,
        'w': 14,
    },
    {
        'number': 4,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': null,
        's': 3,
        'e': 5,
        'w': 15,
    },
    {
        'number': 5,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': null,
        's': null,
        'e': 6,
        'w': 4,
    },
    {
        'number': 6,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': null,
        's': 7,
        'e': null,
        'w': 5,
    },
    {
        'number': 7,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 6,
        's': 8,
        'e': null,
        'w': null,
    },
    {
        'number': 8,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 7,
        's': 9,
        'e': null,
        'w': 1,
    },
    {
        'number': 9,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 8,
        's': null,
        'e': null,
        'w': 10,
    },
    {
        'number': 10,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 1,
        's': null,
        'e': 9,
        'w': 11,
    },
    {
        'number': 11,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 2,
        's': null,
        'e': 10,
        'w': 12,
    },
    {
        'number': 12,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 13,
        's': null,
        'e': 11,
        'w': null,
    },
    {
        'number': 13,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 14,
        's': 12,
        'e': 2,
        'w': null,
    },
    {
        'number': 14,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': 15,
        's': 13,
        'e': 3,
        'w': null,
    },
    {
        'number': 15,
        'name': 'The river',
        'environment': 'Water rushing at splashing in front of you',
        'n': null,
        's': 14,
        'e': 4,
        'w': null,
    },
]