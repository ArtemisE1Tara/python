import random

#player1 = input('Player 1 name: ')
#player2 = input('Player 2 name: ')
player1 = 'tessa'
player2 = 'nick'
x = 1687
#x = float(input('Number of rounds to be played: '))

roundCount = 0
player_1_winCount = 0
player_2_winCount = 0

while roundCount<=x:
    player_1_rollValue = random.randint(1,6)
    player_2_rollValue = random.randint(1,6)

    if player_1_rollValue>player_2_rollValue:
        player_1_winCount = player_1_winCount + 1
    else:
        player_2_winCount = player_2_winCount + 1
    roundCount = roundCount + 1

if player_1_winCount>player_2_winCount:
    print(f'{player1} wins!')
elif player_2_winCount>player_1_winCount:
    print(f'{player2} wins!')
elif player_2_winCount>player_1_winCount:
    print(f"It's a tie!")


