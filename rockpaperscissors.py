import random

your_move = input('Please choose a move: ')
moves = ['rock', 'paper', 'scissors']
random_move = random.choice(moves)

if random_move == 'rock' and your_move == 'paper':
    print('The computer chose rock! You win')
elif random_move == 'rock' and your_move == 'scissors':
    print('Computer chose rock! You lose!')
elif random_move == 'scissors' and your_move == 'rock':
    print('Computer chose scissors! You win!')
elif random_move == 'scissors' and your_move == 'paper':
    print('Computer chose scissors! You lose!')
elif random_move == 'paper' and your_move == 'scissors':
    print('Computer chose paper! You win!')
elif random_move == 'paper' and your_move == 'rock':
    print('Computer chose paper! You lose!')
elif random_move == your_move:
    print('Draw')
else:
    print('Choose from rock, paper, and scissors!')
