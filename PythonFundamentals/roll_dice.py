import random

user_choice = int(input('enter your number to roll'))
computer_choice = random.randint(1,6)

if computer_choice == user_choice:
    print('correct!!')
else:
    print('wrong! Try again ?')