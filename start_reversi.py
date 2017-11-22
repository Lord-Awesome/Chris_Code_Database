from __init__ import *
def start_reversi(train, iterations, print_bool_no, black_input_no, white_input_no, print_bool_yes, black_input_yes, white_input_yes, reset_weight_grid_boolean, display_on_lights_boolean, number_of_games, sleep_time, R_value_black, G_value_black, B_value_black, R_value_white, G_value_white, B_value_white, divisor):
    # Program starts here. You can choose between playing a single game, and training the computer against itself over n iterations


    #path = "C:\\Users\\myran\\Desktop" #change for pi
    #os.chdir(path)

    from play_a_game import play_a_game
    from board_setup import board_setup
    from reset_weight_grid import reset_weight_grid
    if reset_weight_grid_boolean == 1:
        reset_weight_grid()  # resets the weight_grid

    #train = 'no' #Option to train the computer. If no, it plays a single game. If yes, it plays 'iterations' games. print_bool determines if it the program displays output. Recommend 0 for training

    print("White RBG: ", R_value_white, B_value_white, G_value_white)
    print("Black RBG: ", R_value_black, B_value_black, G_value_black)

    if train == 'no':
        board = board_setup()
        #print_bool_no = 1
        #black_input_no = 'starter_input'
        #white_input_no = 'starter_input'
        if print_bool_no == 1:
            print('Starting board state: ')
            print(board)
        for i in range(number_of_games):
            pixels.clear()
            [board, board_original] = board_setup()
            winner = play_a_game(board, print_bool_no, black_input_no, white_input_no,display_on_lights_boolean, sleep_time, R_value_black, G_value_black, B_value_black, R_value_white, G_value_white, B_value_white, divisor, board_original)
        x = input('Press Enter to Exit')

    if train == 'yes':
        #iterations = 1000
        #print_bool_yes = 0
        #black_input_yes = 'computer_weight_capture'
        #white_input_yes = 'computer_random'
        
        winner_list = []
        black_wins = 0
        white_wins = 0
        tie_wins = 0
        
        for game in range(iterations):
            print('-'*100)
            print('                Game ', game+1)
            print('-'*100)

            [board, board_original] = board_setup()
            pixels.clear()
            winner = play_a_game(board, print_bool_yes, black_input_yes, white_input_yes, 0, 0, R_value_black, G_value_black, B_value_black, R_value_white, G_value_white, B_value_white, divisor, board_original)

            winner_list.append(winner)

            if winner == 'black':
                black_wins += 1
            if winner == 'white':
                white_wins += 1
            if winner == 'tie':
                tie_wins += 1

        print('-' * 100)
        print('-' * 100)
        print('-' * 100)
        print('-' * 100)
              
        print('Weight Grid Summary')
        final_weight_grid = np.load('weight_grid.npy')
        if np.min(np.abs(final_weight_grid)) != 0:
            normalized_grid = np.true_divide(final_weight_grid, np.min(np.abs(final_weight_grid)))
        else:
            normalized_grid = final_weight_grid
        print(normalized_grid)
            
        print('Winning Summary')
        print('Black wins: ', black_wins)
        print('White wins: ', white_wins)
        print('Tie: ', tie_wins)
        print('-'*100)

        for i in range(number_of_games):
            board = board_setup()
            pixels.clear()
            winner = play_a_game(board, print_bool_no, black_input_yes, white_input_yes, display_on_lights_boolean, sleep_time, R_value_black, G_value_black, B_value_black, R_value_white, G_value_white, B_value_white, divisor, board_original)

        



