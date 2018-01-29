#from IPython.display import clear_output
import random

def display_board(board):
    #clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#display_board(['O','X','O','X','O','X','O','X','O','O'])

def win_check(board, marker):
    return (board[7] == board[8] == board[9] == marker or
        board[4] == board[5] == board[6] == marker or
        board[1] == board[2] == board[3] == marker or
        board[7] == board[4] == board[1] == marker or
        board[8] == board[5] == board[2] == marker or
        board[9] == board[6] == board[3] == marker or
        board[7] == board[5] == board[3] == marker or
        board[9] == board[5] == board[1] == marker)

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('0','X')

def place_marker(board, marker, position):
    board[position] = marker

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
    #while position not in range(1,10) or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

