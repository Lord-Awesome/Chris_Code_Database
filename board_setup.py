from __init__ import *
def board_setup():
    
    board = np.zeros([8,8])
    board[3,3] = 1 #white
    board[4,3] = 2 #black
    board[3,4] = 2
    board[4,4] = 1
    board_original = board.copy()


    return [board, board_original]
