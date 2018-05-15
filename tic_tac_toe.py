from pprint import pprint

board_game = [['-'] * 3 for i in range(3)]
is_finish = False


def show_board_game():
    for i in range(3):
        pprint(board_game[i])

def turn_X():
    first_pass = True
    row = 0
    col = 0
    while first_pass or board_game[row][col] == '-':
        first_pass = False
        num = input('Player X: ')
        row,col = num.split(',')
        row = int(row)
        col = int(col)
        board_game[row][col] = 'X'
        
        show_board_game()


def turn_O():
    first_pass = True
    row = 0
    col = 0
    while first_pass or board_game[row][col] == '-':
        first_pass = False
        num = input('Player O: ')
        row,col = num.split(',')
        row = int(row)
        col = int(col)
        board_game[row][col] = 'O'

        show_board_game()


def check(player):
    if board_game[0][0] == player and board_game[0][1] == player and board_game[0][2] == player:
        return True
    elif board_game[0][0] == player and board_game[1][0] == player and board_game[2][0] == player:
        return True
    elif board_game[0][0] == player and board_game[1][1] == player and board_game[2][2] == player:
        return True
    elif board_game[0][2] == player and board_game[1][1] == player and board_game[2][0] == player:
        return True
    elif board_game[0][2] == player and board_game[1][2] == player and board_game[2][2] == player:
        return True
    elif board_game[2][0] == player and board_game[2][1] == player and board_game[2][2] == player:
        return True
    

def start_game():
    for _ in range(9):
        turn_X()
        is_finish = check('X')
        if is_finish == True:
            pprint('Winner is player X')
            return   
        turn_O()
        is_finish = check('O')
        if is_finish == True:
            pprint('Winner is player O')
            return

start_game()


