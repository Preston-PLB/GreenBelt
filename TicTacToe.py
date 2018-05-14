
"""
Variables
"""
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

player1_turn = True


"""
Functions
"""
def is_win(board_state, player):
    for x in range(3):
        if board_state[x][0] == player and board_state[x][1] == player and board_state[x][2] == player:
            return True
        elif board_state[0][x] == player and board_state[1][x] == player and board_state[2][x] == player:
            return True

    if board_state[0][0] == player and board_state[1][1]  == player and board_state[2][2] == player:
        return True
    elif board_state[0][2] == player and board_state[1][1]  == player and board_state[2][0] == player:
        return True
    else:
        return False


def get_letter(board, y, x):
    codes = ['O', ' ', 'X']
    if board[y][x] != 0:
        return codes[board[y][x]+1]
    else:
        return y*3+x+1


def print_board(board):
    print(' ', get_letter(board, 0, 0), ' | ', get_letter(board, 0, 1), ' | ', get_letter(board, 0, 2))
    print('-----------------')
    print(' ', get_letter(board, 1, 0), ' | ', get_letter(board, 1, 1), ' | ', get_letter(board, 2, 2))
    print('-----------------')
    print(' ', get_letter(board, 2, 0), ' | ', get_letter(board, 2, 1), ' | ', get_letter(board, 2, 2))


def can_move(board, move):
    if move >= 9 or move < 0:
        return False

    movex = move % 3
    movey = move // 3

    if board[movey][movex] != 0:
        return False
    else:
        return True


def make_move(board, move, player_token):
    movex = move % 3
    movey = move // 3

    board[movey][movex] = player_token


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

    move = int(input("Where would you like to move?"))-1

    if can_move(board, move):
        make_move(board, move, player_token)
    else:
        print('\n\n\n\n\n')
        excuse = input('You cannot move to ' + str(move) + '. Press ENTER to continue')

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

