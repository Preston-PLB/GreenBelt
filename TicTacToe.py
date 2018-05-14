"""
Variables
"""
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

player1_turn = True

"""
Functions
"""
def get_letter(board, pos):
    codes = ['O', ' ', 'X']
    if board[pos] != 0:
        return codes[board[pos] + 1]
    else:
        return pos


"""
Main Program
"""
while True:

    print('\n\n\n\n\n')
    print(' ', get_letter(board, 0), ' | ', get_letter(board, 1), ' | ', get_letter(board, 2))
    print('-----------------')
    print(' ', get_letter(board, 3), ' | ', get_letter(board, 4), ' | ', get_letter(board, 5))
    print('-----------------')
    print(' ', get_letter(board, 6), ' | ', get_letter(board, 7), ' | ', get_letter(board, 8))
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

    if move < 9 or move >= 0 or board[move] == 0:
        board[move] = player_token
    else:
        print('\n\n\n\n\n')
        excuse = input('You cannot move to ' + str(move) + '. Press ENTER to continue')
        continue

    is_win = False

    for x in range(3):
        if board[x * 3 + 0] == player_token and board[x * 3 + 1] == player_token and board[x * 3 + 2] == player_token:
            is_win = True
            break
        elif board[x] == player_token and board[x + 3] == player_token and board[x + 6] == player_token:
            is_win = True
            break
        elif board[0] == player_token and board[4] == player_token and board[8] == player_token:
            is_win = True
            break
        elif board[6] == player_token and board[4] == player_token and board[2] == player_token:
            is_win = True
            break

    if is_win:
        print('\n\n\n\n\n')
        print(' ', get_letter(board, 0), ' | ', get_letter(board, 1), ' | ', get_letter(board, 2))
        print('-----------------')
        print(' ', get_letter(board, 3), ' | ', get_letter(board, 4), ' | ', get_letter(board, 5))
        print('-----------------')
        print(' ', get_letter(board, 6), ' | ', get_letter(board, 7), ' | ', get_letter(board, 8))
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

