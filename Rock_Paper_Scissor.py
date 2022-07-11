import random

choices = [1, 2, 3]
actions = ['rock', 'paper', 'scissors']

while True:
    action1 = input("Enter a choice (1. rock, 2. paper, 3. scissor), 'q' to exit: ")
    action2 = random.choice(choices)

    if action1 == 'q':
        break
    
    action1 = int(action1)
    if action1 in choices:
        print(f'\rYou chose [{actions[action1-1]}], computer chose [{actions[action2-1]}].....', end='')
        if action1 == action2:
            print("Tie!")
        elif (action1 > action2) or (action1 == 1 and action2 == 3):
            print('You win!')
        else:
            print('You lose!')