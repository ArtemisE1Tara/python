import random

targetValue = float(input('Enter target score: '))

player1 = input('Player 1 name: ')
player2 = input('Player 2 name: ')

player1_rollValue = 0
player2_rollValue = 0
player1_total = 0
player2_total = 0

while player1_total<targetValue and player2_total<targetValue:
    player1_rollValue = random.randint(1,6)
    player2_rollValue = random.randint(1,6)

    player1_total = player1_rollValue + player1_total
    player2_total = player2_rollValue + player2_total

if player1_total>player2_total:
    print(f"{player1} wins!\n{player1}'s score: {player1_total}\n{player2}'s score: {player2_total}")
elif player2_total>player1_total:
    print(f"{player2} wins!\n{player2}'s score: {player2_total}\n{player1}'s score: {player1_total}")
elif player2_total==player1_total:
    print("It's a tie!\n{player1}'s score: {player1_total}\n{player2}'s score: {player2_total}")


