"""
Variables
"""
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

player1_turn = True


"""
Functions
"""
def is_win(board_state, player):
    for x in range(3):
        if board_state[x*3+0] == player and board_state[x*3+1] == player and board_state[x*3+2] == player:
            return True
        elif board_state[x] == player and board_state[x+3] == player and board_state[x+6] == player:
            return True

    if board_state[0] == player and board_state[4] == player and board_state[8] == player:
        return True
    elif board_state[6] == player and board_state[4] == player and board_state[2] == player:
        return True
    else:
        return False


def get_letter(board, pos):
    codes = ['O', ' ', 'X']
    if board[pos] != 0:
        return codes[board[pos]+1]
    else:
        return pos


def print_board(board):
    print(' ', get_letter(board, 0), ' | ', get_letter(board, 1), ' | ', get_letter(board, 2))
    print('-----------------')
    print(' ', get_letter(board, 3), ' | ', get_letter(board, 4), ' | ', get_letter(board, 5))
    print('-----------------')
    print(' ', get_letter(board, 6), ' | ', get_letter(board, 7), ' | ', get_letter(board, 8))


def can_move(board, move):
    if move >= 9 or move < 0:
        return False

    if board[move] != 0:
        return False
    else:
        return True


def make_move(board, move, player_token):
    board[move] = player_token


"""
Main Program
"""
while True:

    print('\n\n\n\n\n')
    print_board(board)
    print('\n\n')
    player_token = 0
    if player1_turn:
        player_token = 1
    else:
        player_token = -1

    move = (input("Where would you like to move?"))

    try:
        move = int(move)
    except ValueError:
        print('\n\n\n\n\n')
        excuse = input('You cannot move to ' + move + '. Press ENTER to continue')
        continue

    if can_move(board, move):
        make_move(board, move, player_token)
    else:
        print('\n\n\n\n\n')
        excuse = input('You cannot move to ' + str(move) + '. Press ENTER to continue')
        continue

    if is_win(board, player_token):
        print('\n\n\n\n\n')
        print_board(board)
        print('\n\n')

        winner = ''

        if player1_turn:
            winner = 'Player 1'
        else:
            winner = 'Player 2'

        print('CONGRATS! ', winner, 'WINS!!!!')

        break
    else:
        player1_turn = not player1_turn
