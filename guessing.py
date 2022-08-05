import random
computers_number=random.randint(1,50)
prompt='What is your guessing? '
while True:
    players_guess=input(prompt)
    if computers_number==int(players_guess):
        print('Correct! ')
        break
    elif computers_number>int(players_guess):
        print('Too loww!')
    else:
        print("Too high!")