"""

All environments of this game are located here.
Controls for the game is n for north, s for south, e for east and
finally - w for west. Numbers in dictionary is corrensponding to
the environment which you are navigating to.

"""

null = ''
env_list = [

    {
        'number': 0,
        'name': 'The Tent',
        'scenario': 'green tent sheets(walls), a red sleeping bag, a hat with'
                    ' a feather',
        'step outside': 1,
    },
    {
        'number': 1,
        'name': 'The Tent Entrance',
        'scenario': 'You are standing outside your tent. \nYou can now'
                    ' navigate by typing directions "n"(north), "s"(south), '
                    '"e"(east) or "w"(west)',
        'n': 0,
        's': 10,
        'e': 8,
        'w': 2,

    },
    {
        'number': 2,
        'name': 'The Birch',
        'scenario': 'You step up to a majestic but tired old birch. A birch'
                    ' is a white tree with black spots on it. To your left '
                    'is a bridge that stretches over the wild river.',
        'n': 3,
        's': 11,
        'e': 1,
        'w': 13,
    },
    {
        'number': 3,
        'name': 'The Path with the faun',
        'scenario': 'You walk along a path, a not so very clear path. You '
                    'stop when you suddenly see what you think is a faun. '
                    'Just one second later the "faun" is gone. What was that?',
        'n': 4,
        's': 2,
        'e': null,
        'w': 14,
    },
    {
        'number': 4,
        'name': 'The Waterfall',
        'scenario': 'You end up at a cliff. You can not walk further north.'
                    ' If you lose your focus now it could be fatal.',
        'n': null,
        's': 3,
        'e': 5,
        'w': 15,
    },
    {
        'number': 5,
        'name': 'The Path with cloudberrys',
        'scenario': 'You continue your journey along the path. You say to '
                    'yourself that it is safest this way. On the ground you'
                    ' see beutiful small orange and red cloudberries.',
        'n': null,
        's': null,
        'e': 6,
        'w': 4,
    },
    {
        'number': 6,
        'name': 'The Wall',
        'scenario': 'The path you have been taken is making an abrupt stop'
                    ' just when it hits a mountain wall. '
                    'You can only go south and west from here',
        'n': null,
        's': 7,
        'e': null,
        'w': 5,
    },
    {
        'number': 7,
        'name': 'The Forest.',
        'scenario': 'You step into a dark dark forest with a strange'
                    ' strange smell',
        'n': 6,
        's': 8,
        'e': null,
        'w': null,
    },
    {
        'number': 8,
        'name': 'The Deeper Forest',
        'scenario': 'You seem lost. You have gone longer into the dark '
                    'smelly forest when you suddenly see some light to '
                    'the south. Your nose tells you to go where the light is.',
        'n': 7,
        's': 9,
        'e': null,
        'w': 1,
    },
    {
        'number': 9,
        'name': 'The Fence',
        'scenario': 'My goodness. You thought that you would never come '
                    'out of that forest, but here you are. Impossible to '
                    'go more south since there is a mystical red fence '
                    'blocking the way',
        'n': 8,
        's': null,
        'e': null,
        'w': 10,
    },
    {
        'number': 10,
        'name': 'The Beach',
        'scenario': 'What the heck? You all of a suddden find yourself '
                    'at a beach. Just by a lake with people waterskiing '
                    'out there but you can not see who they are.',
        'n': 1,
        's': null,
        'e': 9,
        'w': 11,
    },
    {
        'number': 11,
        'name': 'The Jetty',
        'scenario': 'You walk along the beach until you come to a jetty. '
                    'The boat that they use for water-sports must come '
                    'from this jetty. You see footsteps made out of '
                    'water on the wooden jetty.',
        'n': 2,
        's': null,
        'e': 10,
        'w': 12,
    },
    {
        'number': 12,
        'name': 'The Fireplace',
        'scenario': 'This is the furtherest to the west as you can come. '
                    'You see drunk people sitting by a fireplace. '
                    'They are playing guitar, accordion and '
                    'cooking food at the same time. '
                    'They seem very happy.',
        'n': 13,
        's': null,
        'e': 11,
        'w': null,
    },
    {
        'number': 13,
        'name': 'The River',
        'scenario': 'You walk on the bridge, scared but stubborn as you '
                    'cross it. You are now at the east side of the river',
        'n': 14,
        's': 12,
        'e': 2,
        'w': null,
    },
    {
        'number': 14,
        'name': 'The Scaur',
        'scenario': 'You come to a full stop as you reach a very very high '
                    'and steep cliff. It is considered very '
                    'dangerous to continue north',
        'n': 15,
        's': 13,
        'e': 3,
        'w': null,
    },
    {
        'number': 15,
        'name': 'The Fall',
        'scenario': 'You feel helpless as you step out the waterfall. Is '
                    'this it? The cold water and you are suddenly racing '
                    'against each other vertically. This is the end',
        'n': null,
        's': null,
        'e': null,
        'w': null,
    },
]
