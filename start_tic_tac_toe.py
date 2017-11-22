from __init__ import *
from tic_tac_toe_1 import *
def start_tic_tac_toe(display_on_lights_boolean, display_on_lights_train_boolean, summary_print_bool, input_number_of_trains, input_number_of_games, x_win_weighting, o_win_weighting, sleep_time, sleep_time_train, divisor):
    import random
    import time
    import itertools
    import pickle
    import math

    # if display_on_lights_boolean == 1:
    #     import Adafruit_WS2801
    #     import Adafruit_GPIO.SPI as SPI

    #input_number_of_trains = int(input("How many games would you like to play to train? ==> "))
    #input_number_of_games = int(input("How many games would you like to play per iteration? ==> "))
    X_wins_list = []
    O_wins_list = []
    draw_wins_list = []
    # global x_play_with_weights_bool
    # global o_play_with_weights_bool
    # global x_play_with_weights
    # global o_play_with_weights

    #summary_print_bool = True

    # try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)  

    pixels.clear()
    # pixels.set_pixel(0,RGB_to_color(100,100,100,1))
    pixels.show() 
    # except Exception as ex:
        # print(ex)
        # print("Error Encountered")


    for j in range(1):
        for i in range(1):
            #print("Iteration ", (100*j)+i+1, ". Win weighting is ", j+1, " and lose weighting is ", i+1)
            #lose_weighting = i+1
            #win_weighting = j+1

            # ----------------------------------- Execute Training --------------------------------------------------------------- #
            x_play_with_weights_bool = False
            o_play_with_weights_bool = False
            print_once_per_game_bool = False
            print_every_move_bool = False  
            number_of_games = input_number_of_trains
            print("Training...")
            [X_wins, O_wins, draw_wins] = tic_tac_toe_1(x_play_with_weights_bool, o_play_with_weights_bool, number_of_games, x_win_weighting, o_win_weighting, summary_print_bool, print_once_per_game_bool, print_every_move_bool, display_on_lights_train_boolean, sleep_time_train, divisor)
            # [X_wins, O_wins, draw_wins] = play_games(x_play_with_weights_bool, o_play_with_weights_bool, number_of_games, x_win_weighting, o_win_weighting, summary_print_bool, print_once_per_game_bool, print_every_move_bool, display_on_lights_train_boolean, sleep_time_train, divisor)


            # ----------------------------------- Execute Playing --------------------------------------------------------------- #
            x_play_with_weights_bool = True
            o_play_with_weights_bool = True
            print_once_per_game_bool = False
            print_every_move_bool = False
            number_of_games = input_number_of_games
            print("Playing...")
            [X_wins, O_wins, draw_wins] = tic_tac_toe_1(x_play_with_weights_bool, o_play_with_weights_bool, number_of_games, x_win_weighting, o_win_weighting, summary_print_bool, print_once_per_game_bool, print_every_move_bool, display_on_lights_train_boolean, sleep_time_train, divisor)
            # [X_wins, O_wins, draw_wins] = play_games(x_play_with_weights_bool, o_play_with_weights_bool, number_of_games, x_win_weighting, o_win_weighting, summary_print_bool, print_once_per_game_bool, print_every_move_bool, display_on_lights_boolean, sleep_time, divisor)

            X_wins_list.append(X_wins)
            O_wins_list.append(O_wins)
            draw_wins_list.append(draw_wins)

    if 0:
        print("---------------------------------------\n\n")

        print("X wins list: ", X_wins_list)
        print("O wins list: ", O_wins_list)
        print("Draw list: ", draw_wins_list)

        print("---------------------------------------\n\n")

    #print("Best win weighting is ", 1*math.floor(X_wins_list.index(max(X_wins_list))/100), "and best lose weighting is ", ((X_wins_list.index(max(X_wins_list))%100)*1)," with a win percentage of ", max(X_wins_list)/(number_of_games*0.01), "%")
