from rooms import rooms_list

player_name = 'player'
game_question = ''
begin_game = ''

def print_lines():
    print('--------------------------------------------------')
    print('--------------------------------------------------')

def intro():
    print_lines()
    print('Welcome to this peaceful, mysterious space in time')
    print_lines()

def get_player_name():
    player_name = str(input('Please enter your name:\n'))
    if player_name == '':
        player_name = 'James Pond'
        print('Well, as you did not tell me your name I will just call you James Pond.')
    print(f'Nihaody, {player_name}!')
    return player_name

def beginning():
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

def validate_answer(game_question):
    while True:
        print(game_question)

def game():
    intro()
    get_player_name()
    beginning()
    directions = ['n', 's', 'e', 'w']
    answer = ['yes', 'no']

    print('POFF! You wake up. Smoke is around you but disappearing. You find yourself lying inside a green tent. What do you want to do?')
    game_question = str(input('Do you want to step outside the tent? "yes" or "no"?\n'))
    while game_question != answer:
        return game_question
    if game_question == 'yes':
            return(rooms_list[1]['environment'])

game()
print(rooms_list[1]['environment'])