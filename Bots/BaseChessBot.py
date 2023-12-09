
#
#   Example function to be implemented for
#       Single important function is next_best
#           color: a single character str indicating the color represented by this bot ('w' for white)
#           board: a 2d matrix containing strings as a descriptors of the board '' means empty location "XC" means a piece represented by X of the color C is present there
#           budget: time budget allowed for this turn, the function must return a pair (xs,ys) --> (xd,yd) to indicate a piece at xs, ys moving to xd, yd
#

from PyQt6 import QtCore

#   Be careful with modules to import from the root (don't forget the Bots.)
from Bots.ChessBotList import register_chess_bot

#   Simply move the pawns forward and tries to capture as soon as possible
def chess_bot(player_sequence, board, time_budget, **kwargs):

    king_moves = [(1,0),(-1,0),(0,1),(0,-1)]
    color = player_sequence[1]
    x = range(board.shape[0]-1)
    y = range(board.shape[1])
    for x in range(board.shape[0]-1):
        for y in range(board.shape[1]):
            """if board[x,y] != "p"+color:
                continue
            if y > 0 and board[x+1,y-1] != '' and board[x+1,y-1][-1] != color:
                return (x,y), (x+1,y-1)
            if y < board.shape[1] - 1 and board[x+1,y+1] != '' and board[x+1,y+1][1] != color:
                return (x,y), (x+1,y+1)
            elif board[x+1,y] == '':
                return (x,y), (x+1,y)"""
            if board[x,y] != "k"+color:
                continue
            for move in king_moves:
                new_x, new_y = x + move[0], y+move[1]
                return (x, y), (new_x, new_y)


    return (0,0), (0,0)

#   Example how to register the function
register_chess_bot("Testingmy p", chess_bot)
