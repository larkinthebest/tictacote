board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

game_still = True
winner = None
current_player = 'X'
def play_game():
    display_board()
    while game_still:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()
    if winner == "X" or winner == "O":
        print(winner + ' won')
    elif winner == None:
        print("tie")


def handle_turn(player):
    global board
    print(player + "'s turn")
    position = input('choose position from 1 to 9: ')

    valid = False
    while not valid:
        while position not in ['1',"2","3",'4',"5",'6',"7",'8',"9"]:
            position = input('choose correct position: ')

        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print('you cant put anything there! ')

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner

    row_winner = check_rows()
    columns_winner = check_columns()
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return

def check_rows():
    global game_still

    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_still = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still

    column_1 = board[0] == board[4] == board[8] != '-'
    column_2 = board[1] == board[5] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        game_still = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still

    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[2] == board[4] != '-'

    if diagonal_1 or diagonal_2:
        game_still = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_still
    if '-' not in board:
        game_still = False

    return

def flip_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

play_game()