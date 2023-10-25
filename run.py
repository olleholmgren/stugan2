import sys
import time
from environments import env_list

player_name = 'player'
game_question = ''
text = ''
text_being_printed = False


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
    slow_print('Welcome to this peaceful, mysterious space in time')
    print_lines()


def get_player_name():

    """
    Register the name of the player
    """

    global player_name
    player_name = str(input('Please enter your name:\n'))
    if player_name == '':
        player_name = 'James Pond'
        slow_print('Well, as you did not tell me your name I '
                   'will just call you James Pond.')
    slow_print(f'Nihaody, {player_name}!')
    return player_name


def intro():

    """
    Introduce the player and give instructions
    """

    global game_question
    condition = str(input(f'How are you feeling today, {player_name}?\n'))
    condition_follow_up1 = str(input(f'I see, why do you think you are feeling'
                                     f' {condition}?\n'))
    condition_follow_up2 = str(input('Alright. . . Well, do you want to talk '
                                     'to me about it?\n'))
    slow_print('Ok. I totally understand.')
    game_question = str(input(f'Do you want to play an adventure game with me '
                              f'{player_name}?\n'))

    if game_question == 'yes':
        slow_print('Ok, lets go!')
    else:
        slow_print('Oh, I see. Well, I hope you get better soon.')
        slow_print('Please come back another time. Bye for now!')
        slow_print('--------------------------------------------------')
        slow_print('Game over!')
        slow_print('--------------------------------------------------')
        sys.exit()

    time.sleep(1)
    print_lines()
    slow_print('Firstly, let me tell you how to play the game')
    print_lines()
    slow_print('You navigate by giving me a command of direction.\nn '
               'for north, s for south, e for east and w for west.\nYou can '
               'answer questions with "yes" or "no"')
    slow_print('Hit ENTER to continue')


def navigate(env_number):

    """
    Navigate the paths through all environments
    """

    print_lines()
    slow_print(env_list[env_number]['name'])
    print_lines()
    time.sleep(1)
    slow_print(env_list[env_number]['scenario'])
    time.sleep(1)

    if env_number == 15:
        slow_print('--------------------------------------------------')
        slow_print('Game over!')
        slow_print('--------------------------------------------------')
        sys.exit()

    valid_way = build_way(env_number)

    while True:
        try:
            direction = input('')
            if direction not in valid_way:
                raise ValueError(f'Hey, that is not a valid direction from '
                                 f'this location. Pick one of these, '
                                 f'please: {valid_way}')
            navigate(env_list[env_number][direction])
        except KeyError:
            slow_print(f'Hey, that is not a valid direction from this '
                       f'location. Pick one of these, please: {valid_way}')
        except ValueError as e:
            slow_print(str(e))
        navigate(env_number)


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


def slow_print(text):

    """
    Print out presented text in a slower motion
    """

    global text_being_printed
    text_being_printed = True
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    text_being_printed = False
    print('')


def prevent_input():

    """
    Get input from the player while preventing input during slow printing
    """

    while True:
        user_input = input()
        if not text_being_printed:
            return user_input
        else:
            slow_print("Hey! Please wait for me to finish")


def game():

    """
    Main function to run the game
    """
    
    slow_print(text)
    greet()
    get_player_name()
    intro()
    answer = ['yes', 'no']
    user_input = prevent_input()

    slow_print('POFF!')
    time.sleep(1)
    slow_print('You wake up.')
    time.sleep(1)
    slow_print('Smoke is around you but disappearing.')
    time.sleep(1)
    slow_print('You find yourself lying inside a green tent. What do you want '
               'to do?')
    time.sleep(1)
    game_question = input('Do you want to step outside the tent? "yes" or '
                          '"no"?\n')

    while game_question not in answer:
        slow_print('Invalid input, please type "yes" or "no"')
        time.sleep(1)
        game_question = input('Do you want to step outside the tent? "yes" or '
                              '"no"?\n')

    if game_question == 'yes':
        navigate(1)
    else:
        slow_print('Ok, that is fine. You can stay in the tent.')
        slow_print('I have to go now. Please come back another time!')
        slow_print('--------------------------------------------------')
        slow_print('Game over!')
        slow_print('--------------------------------------------------')
        sys.exit()


if __name__ == '__main__':
    game()
