import sys
from rooms import env_list

player_name = 'player'
game_question = ''


def print_lines():

    """
    Style the game with lines
    """

    print('--------------------------------------------------')
    print('--------------------------------------------------')


def greet():

    """
    Greet the player
    """

    print_lines()
    print('Welcome to this peaceful, mysterious space in time')
    print_lines()


def get_player_name():

    """
    Register the name of the player
    """

    global player_name
    player_name = str(input('Please enter your name:\n'))
    if player_name == '':
        player_name = 'James Pond'
        print('Well, as you did not tell me your name I will just call you James Pond.')
    print(f'Nihaody, {player_name}!')
    return player_name


def intro():

    """
    Introduce the player and give instructions
    """

    global game_question
    condition = str(input(f'How are you feeling today, {player_name}?\n'))
    condition_follow_up1 = str(input(f'I see, why do you think you are feeling {condition}?\n'))
    condition_follow_up2 = str(input('Alright. . . Well, do you want to talk to me about it?\n'))
    print('Ok. I totally understand.')
    game_question = str(input(f'Do you want to play an adventure game with me {player_name}?\n'))
    if game_question == 'yes':
        print('ok, lets go!')
    else: 
        print('oh I see')
    print_lines()
    print('Firstly, let me tell you how to play the game')
    print_lines()
    print('You navigate by giving me a command of direction.\nn for north, s for' 
          'south, e for east and w for west.\nYou can answer questions with "yes" or "no"')


def game():

    """
    Main function to run the game
    """

    greet()
    get_player_name()
    intro()
    directions = ['n', 's', 'e', 'w']
    answer = ['yes', 'no']

    print('POFF! You wake up. Smoke is around you but disappearing. You find yourself lying inside a green tent. What do you want to do?')
    game_question = input('Do you want to step outside the tent? "yes" or "no"?\n')
    while game_question not in answer:
        print('Invalid input, please type "yes" or "no"')
        game_question = input('Do you want to step outside the tent? "yes" or "no"?\n')
    if game_question == 'yes':
        navigate(1)
    else:
        print('Ok, that is fine. You can stay in the tent')


def navigate(env_number):

    """
    Navigate the paths through all environments
    """
    
    print_lines()
    print(env_list[env_number]['name'])
    print(env_list[env_number]['scenario'])
    if env_number == 15:
        print('Game over!')
        sys.exit()
    valid_way = build_way(env_number)
    direction = input('')
    if direction not in valid_way:
        print(f'Hey, that is not a valid direction from this location. Pick one of these, please: {valid_way}')
        direction = input('')
    navigate(env_list[env_number][direction])


def build_way(env_number):

    """
    Build the way for the navigate function and list the possible direction
    """

    valid_way = []
    if env_list[env_number]['n']:
        valid_way.append('n')
    if env_list[env_number]['s']:
        valid_way.append('s')
    if env_list[env_number]['e']:
        valid_way.append('e')
    if env_list[env_number]['w']:
        valid_way.append('w')
    return valid_way


# Run the game
game()
