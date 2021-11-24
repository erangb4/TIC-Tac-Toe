def player(i):  # the function return the player in this turn
    if i % 2 == 0:
        return 'x'
    return 'o'


def legal(place, open_place):      # the function get the input from the player and check if the input is legal,
    if open_place.count(place) == 1:
        open_place.remove(place)
        return place, open_place
    else:                          # else the function get input until the input will be legal
        place = input('your input is illegal.\nplease enter your place again (only numbers): ')
        return legal(place, open_place)


def _set(board, place, i):  # the function set the player in the place that he choose
    a = int(place[0])
    b = int(place[1])
    board[a][b] = player(i)
    return board


def win_check(board, _player):  # the function check if the player that played is winning
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == _player or board[0][i] == board[1][i] == board[2][i] == _player:
            return True
    if board[0][0] == _player and board[1][1] == _player and board[2][2] == _player:
        return True
    if board[0][2] == _player and board[1][1] == _player and board[2][0] == _player:
        return True
    return False


def print_board(board):  # the function print how the board look like right now
    for i in board:
        print('  '.join(i))


def main():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    open_place = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    print_board(board)
    for i in range(9):                                # get the place from the player
        place = input(player(i) + '-player! it is your turn.\nenter your place (only numbers): ')
        place, open_place = legal(place, open_place)  # make sure that the input is legal
        board = _set(board, place, i)                 # put the sign's player in the board
        print_board(board)                            # print board to the next turn
        if win_check(board, player(i)):
            print(player(i) + '-player!! you win!')
            break                                     # if the player won break the loop
        elif i == 8:                                  # if i == 8 its mean that the last turn done
            print('draw')                             # and because the loop didn't break the game end with a draw
    if input('if you want to play again - enter "yes", else press - "enter" ') == 'yes':
        main()                                        # if the player said yes we call to the main again


main()
