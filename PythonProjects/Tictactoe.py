#PROJECT - TIC-TAC-TOE GAME

#Import modules
from IPython.display import clear_output
import random

#Functions
def display_board(board):
    clear_output()
    
    print(' ' + board[1]+' | '+board[2]+' | '+board[3])
    print(' ' + board[4]+' | '+board[5]+' | '+board[6])
    print(' ' + board[7]+' | '+board[8]+' | '+board[9])

def player_input():
    markers = ['X', 'O']
    marker_set = False

    while marker_set == False:
        marker = input('Player 1: Do you want to play with X or O? ').upper()

        if marker not in markers:
            print('Sorry, you entered an incorrect marker. Please choose X or O. ')
        else:
            marker_set = True
    
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while space_check(board, position) == False or position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input('Choose your next position (1-9): '))

    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#Game
print('Welcome to Tic Tac Toe!\n')

while True:
    new_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f'Player 1 chose {player1_marker}\nPlayer 2 chose {player2_marker}\n')
    print(turn + ' will go first!')

    play_game = input('Are you ready to play? Enter Yes or No: ').lower()

    if play_game[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(new_board)
            print('Player 1, it is your turn!')
            position = player_choice(new_board)
            place_marker(new_board, player1_marker, position)

            if win_check(new_board, player1_marker):
                display_board(new_board)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('Unlucky! It is a draw.')
                    break
                else:
                    turn = 'Player 2'
        
        else:
            display_board(new_board)
            print('Player 2, it is your turn!')
            position = player_choice(new_board)
            place_marker(new_board, player2_marker, position)

            if win_check(new_board, player2_marker):
                display_board(new_board)
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('Unlucky! It is a draw.')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break