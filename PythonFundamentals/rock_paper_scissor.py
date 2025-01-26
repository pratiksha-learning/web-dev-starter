import random

user_choice = input('enter your choice from rock, paper and scissor?\n')
computer_choice = random.choice(['rock', 'paper', 'scissor'])

print('computer choice:', computer_choice)
if (user_choice == 'rock' and computer_choice == 'scissor') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissor' and computer_choice == 'paper'):
    print('Its Win!!!!')
elif computer_choice == user_choice:
    print('Its TIE :)')
else:
    print('you lose :(')