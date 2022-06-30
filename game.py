import random


def play():
    user = input("'r' for rock, 's' for scissors, 'p' for paper")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    if winner(user, computer):
        return 'You Won!'
    return 'You Lost'


def winner(player, comp):
    if (player == 'r' and comp == 's') or (player == 's' and comp == 'p') or (player == 'p' and comp == 'r'):
        return True


print(play())
