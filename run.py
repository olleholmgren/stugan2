from rooms import rooms_list




print('\n--------------------------------\n--------------------------------\n\nWelcome to this peaceful,\nmysterious space in time\n\n--------------------------------\n--------------------------------\n')






player_name = str(input('Please enter your name:\n'))
print(f'Nihaody {player_name}!')
condition = str(input(f'How are you feeling today {player_name}?\n'))
condition_follow_up1 = str(input(f'I see, why do you think you are feeling {condition}?\n'))
condition_follow_up2 = str(input('Alright. . . Well, do you want to talk to me about it?\n'))
print('Ok. I totally understand.')
game_question = str(input(f'Do you want to play an adventure game with me {player_name}?\n'))
if game_question == 'yes':
    print('ok, lets go!')
else: print('oh I see')

#print(rooms_list[1]['environment'])