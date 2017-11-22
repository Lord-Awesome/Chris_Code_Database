from __init__ import *
def display_reversi_board_on_lights(board, R_value_black, G_value_black, B_value_black, R_value_white, G_value_white, B_value_white, divisor, board_original):
    from display_leader_on_board import display_leader_on_board
    
    # pixels.clear()


##    black_color = Adafruit_WS2801.RGB_to_color(0,0,255) #green
    black_color = RGB_to_color(R_value_black, B_value_black, G_value_black, divisor)
##    white_color = Adafruit_WS2801.RGB_to_color(255,0,0) #red
    white_color = RGB_to_color(R_value_white, B_value_white, G_value_white, divisor)


    # print("Board original: ", board_original)
    # print("Board new: ", board)
    for i in range(8):
        for j in range(8):
            if (board[i,j] == 1 and board_original[i,j] != 1) or (np.sum(board) == 6 and board[i,j] == 1):
                pixels.set_pixel((16*(i+1))+j+4,white_color)
            if (board[i,j] == 2 and board_original[i,j] != 2) or (np.sum(board) == 6 and board[i,j] == 2):
                pixels.set_pixel((16*(i+1))+j+4,black_color)

    
    # Add border
    if np.sum(board) == 6: ## If it's the first time this display function runs
        border_color = RGB_to_color(0,255,0,divisor)
        for i in range(10):
            pixels.set_pixel(i+3, border_color)
            pixels.set_pixel((9*16)+i+3, border_color)
            pixels.set_pixel((16*i)+3, border_color)
            pixels.set_pixel((16*i)+12, border_color)

    amount_white_greater_than_black = display_leader_on_board(board)
    if amount_white_greater_than_black > 10:
        amount_white_greater_than_black = 10
    elif amount_white_greater_than_black < -10:
        amount_white_greater_than_black = -10

    if amount_white_greater_than_black > 0: ## White is winning
        for i in range(amount_white_greater_than_black):
            pixels.set_pixel(15 + (16*i), white_color)
        for i in range(10 - amount_white_greater_than_black):
            pixels.set_pixel(15 + (16*(9-i)), RGB_to_color(0,0,0,divisor))
    elif amount_white_greater_than_black < 0:
        amount_white_greater_than_black = -1 * amount_white_greater_than_black
        for i in range(amount_white_greater_than_black):
            pixels.set_pixel(15 + (16*i), black_color)
        for i in range(10 - amount_white_greater_than_black):
            pixels.set_pixel(15 + (16*(9-i)), RGB_to_color(0,0,0,divisor))


    pixels.show()


