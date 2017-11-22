from __init__ import *

def start_autonomous_snake(sleep_time, wait_times, number_of_nom_noms, number_of_bombs, number_of_caffeine_pills, level_0_nom_nom, level_1_nom_nom, level_2_nom_nom, display_on_lights_boolean, divisor):



    #This program creates a snake that moves around the board searching for nom-noms (represented in text by the number 99) that spawn randomly. When it eats a nom-nom, it gains length
    # and the nom-nom appears somewhere else. If the snake hits a bomb (usually not visible, but can be set to display as 44), it loses length and the bomb appears somewhere else.
    # The snake looks ahead 3 moves, analyzing each possible path. If it sees a nom-nom in a path, that path gains weight, with the weight value depending on how many moves away the nom-nom is.
    # After analyzing all paths, it chooses the most profitable one and moves to the appropriate square. Then, the process repeats. The snake puts priority on paths that allow it to stay alive the longest.
    # For example, if one path immediately leads to a nom-nom, but the snake will get trapped within the next three moves, it will prefer a path where it doesn't get stuck, as that will end the game.
    # It does this by doing its phase 1 analysis on paths that won't end the game in the next three moves. If there are no such paths, then it moves to phase 2 where it does the same analysis as phase 1,  but looks at all possible paths.


    if display_on_lights_boolean == True:
        pixels.clear()
        pixels.show()

    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
    except Exception as ex:
        print(ex)

    if display_on_lights_boolean == True:
        global nom_nom_color
        global snake_body_color
        global snake_head_color
        global caffeine_pill_color

        nom_nom_color = RGB_to_color(0,255,0,divisor) #blue
        snake_body_color = RGB_to_color(0,0,255,divisor) #green
        snake_head_color = RGB_to_color(255,0,0,divisor) #red
        caffeine_pill_color = RGB_to_color(244,24,66,divisor) #purple
        ## Currently does not display the bombs on the lights to avoid things getting too hectic


    global snake
    global nom_noms
    global bombs
    global caffeine_pills
    global move_count
    global time_position
    global hyper_mode
    global eligible_moves
    global  biggest_value
    global chosen_move
    global the_final_move
    global grid
    global eligible_moves

    snake = [[6,3],[6,4],[6,5],[6,6]]
    nom_noms = [] #Extender pellets
    bombs = []
    caffeine_pills = []
    move_count = 0
    time_position = -1
    hyper_mode = 0
    grid = np.zeros([10,16])
    eligible_moves = []


    generate_starting_positions_of_objects(sleep_time, wait_times, number_of_nom_noms, number_of_bombs, number_of_caffeine_pills, level_0_nom_nom, level_1_nom_nom, level_2_nom_nom, display_on_lights_boolean, divisor)

    execute_moves(sleep_time, wait_times, number_of_nom_noms, number_of_bombs, number_of_caffeine_pills, level_0_nom_nom, level_1_nom_nom, level_2_nom_nom, display_on_lights_boolean, divisor, time_position, hyper_mode)

    
                 
            
    #------------------------------------------------------------------------------------START THE GAME -------------------------------------------------

    # print("Starting snake:")
    # print_snake()
    # time.sleep(sleep_time)

    #------------------------------------------------------------------------------------- THE BIG LOOP -----------------------------------------------------

def generate_starting_positions_of_objects(sleep_time, wait_times, number_of_nom_noms, number_of_bombs, number_of_caffeine_pills, level_0_nom_nom, level_1_nom_nom, level_2_nom_nom, display_on_lights_boolean, divisor):
    while len(nom_noms) < number_of_nom_noms: #randomly place the nom-noms and bombs
        x = random.randint(0,9)
        y = random.randint(0,15)
        if [x,y] not in snake and [x,y] not in nom_noms:
            nom_noms.append([x,y])
            
    while len(bombs) < number_of_bombs:
        x = random.randint(0,9)
        y = random.randint(0,15)
        if [x,y] not in snake and [x,y] not in nom_noms and [x,y] not in bombs:
            bombs.append([x,y])

    while len(caffeine_pills) < number_of_caffeine_pills:
        x = random.randint(0,9)
        y = random.randint(0,15)
        if [x,y] not in snake and [x,y] not in nom_noms and [x,y] not in bombs and [x,y] not in caffeine_pills:
            caffeine_pills.append([x,y])

def execute_moves(sleep_time, wait_times, number_of_nom_noms, number_of_bombs, number_of_caffeine_pills, level_0_nom_nom, level_1_nom_nom, level_2_nom_nom, display_on_lights_boolean, divisor, time_position, hyper_mode):
    move_count = 0
    grid = print_snake()
    new_grid = np.zeros([10,16])
    display_on_lights(new_grid, display_on_lights_boolean, grid)

    while 1:

        move_count = move_count + 1
        
        if len(snake) == 0:
            print("Snake is dead :(")
            break
        
        try:
            chosen_move = make_a_move(sleep_time, wait_times, number_of_nom_noms, number_of_bombs, number_of_caffeine_pills, level_0_nom_nom, level_1_nom_nom, level_2_nom_nom, display_on_lights_boolean, divisor) #This will check to make sure we don't get in trouble but it won't generate a queue so we could forecase one path but then follow another
        except no_more_eligible_moves:
            print_snake()
            print("\n No more eligible moves")
            break
        except secondary_final_move_exception:
            print_snake()
            print("\n Secondary final move = []")
            print(the_final_move)
            print(chosen_move)
            break
        
        snake.append(chosen_move)
        if chosen_move not in nom_noms:
            snake.remove(snake[0])

        check_if_hit_nom_nom(chosen_move, number_of_nom_noms)

        check_if_hit_bomb(chosen_move, number_of_bombs, display_on_lights_boolean)

        [rest_time, time_position_from_function, hyper_mode_from_function] = caffeine_pill(time_position, hyper_mode, sleep_time, wait_times, display_on_lights_boolean)
        time_position = time_position_from_function
        hyper_mode = hyper_mode_from_function
        
        if chosen_move in caffeine_pills:
            caffeine_pills.remove(chosen_move)
            while len(caffeine_pills) < number_of_caffeine_pills:
                x = random.randint(0,9)
                y = random.randint(0,15)
                if [x,y] not in snake and [x,y] not in nom_noms and [x,y] not in eligible_moves and [x,y] not in caffeine_pills:
                    caffeine_pills.append([x,y])

        new_grid = print_snake()
        # print(grid)
        if display_on_lights_boolean == True:
            # display_on_lights(grid, display_on_lights_boolean)
            display_on_lights(grid,display_on_lights_boolean,new_grid)

        time.sleep(rest_time)
        # pixels.clear()
        grid = new_grid

        if display_on_lights_boolean == True:
            try:
                GPIO.output(12,GPIO.HIGH)
                GPIO.output(16, GPIO.HIGH)
            except:
                continue

    print("Number of moves: ", move_count)

def check_if_hit_bomb(chosen_move, number_of_bombs, display_on_lights_boolean):
        if chosen_move in bombs:
            if display_on_lights_boolean == True:
                try:
                    GPIO.output(12,GPIO.LOW)
                    # GPIO.output(16, GPIO.LOW) #Comment out whichever one is yellow
                except:
                    print("GPIO error")
                snake.remove(snake[-1])
                bombs.remove(chosen_move)
        while len(bombs) < number_of_bombs:
            x = random.randint(0,9)
            y = random.randint(0,15)
            if [x,y] not in snake and [x,y] not in nom_noms and [x,y] not in bombs and [x,y] not in eligible_moves:
                bombs.append([x,y])

def check_if_hit_nom_nom(chosen_move, number_of_nom_noms):
    if chosen_move in nom_noms:
            nom_noms.remove(chosen_move)
            while len(nom_noms) < number_of_nom_noms:
                x = random.randint(0,9)
                y = random.randint(0,15)
                if [x,y] not in snake and [x,y] not in nom_noms and [x,y] not in eligible_moves:
                    nom_noms.append([x,y])

def caffeine_pill(time_position, hyper_mode, sleep_time, wait_times, display_on_lights_boolean): #makes the snake go faster for a few moves
        if snake[-1] in caffeine_pills:
            hyper_mode = 1
        if hyper_mode == 1:
            if display_on_lights_boolean == True:
                try:
                    # GPIO.output(12,GPIO.HIGH) #comment out whichever one is blue
                    GPIO.output(16, GPIO.LOW)
                except:
                    print("GPIO error")

            time_position = time_position + 1
            if time_position + 1 == len(wait_times):
                hyper_mode = 0
                time_position = -1
                return(wait_times[-1], time_position, hyper_mode)
            else:
                return(wait_times[time_position], time_position, hyper_mode)
        else:
            return(sleep_time, time_position, hyper_mode)

def print_snake():
    grid = np.zeros([10,16])
    for i in snake:
        grid[i[0]][i[1]] = snake.index(i) + 1
    for i in nom_noms:
        grid[i[0]][i[1]] = 99
    for i in caffeine_pills:
        grid[i[0]][i[1]] = 55
    for i in bombs:
        grid[i[0]][i[1]] = 44
    #os.system("clear")
    # print("\n",grid,"\n")
    return(grid)

def display_on_lights(grid, display_on_lights_boolean, new_grid):

    if display_on_lights_boolean == True:
        for i in range(10):
            for j in range(16):
                my_element = new_grid[i][j]
                if (new_grid[i,j] != grid[i,j]) & (my_element == 99):
                    pixels.set_pixel((16*i)+j,nom_nom_color)
                if (new_grid[i,j] != grid[i,j]) & ([i,j] in snake):
                    if ([i,j] != snake[-1]):
                        pixels.set_pixel((16*i)+j,snake_body_color)
                if (new_grid[i,j] != grid[i,j]) & ([i,j] == snake[-1]):
                    pixels.set_pixel((16*i)+j,snake_head_color)
                if (new_grid[i,j] != grid[i,j]) & (my_element == 55):
                      pixels.set_pixel((16*i)+j,caffeine_pill_color)
                if (new_grid[i,j] != grid[i,j]) & (my_element == 0):
                    pixels.set_pixel((16*i) + j, RGB_to_color(0,0,0,1))
        pixels.show()

def generate_eligible_moves(snake_head, snake):
    eligible_moves = []
    if snake_head[0]-1 >= 0:
        up_location = [snake_head[0]-1, snake_head[1]]
        if up_location not in snake:
            eligible_moves.append(up_location)
            
    if snake_head[0]+1 <= 9:
        down_location = [snake_head[0]+1, snake_head[1]]
        if down_location not in snake:
            eligible_moves.append(down_location)
            
    if snake_head[1]+1 <= 15:
        right_location = [snake_head[0],snake_head[1]+1]
        if right_location not in snake:
            eligible_moves.append(right_location)
            
    if snake_head[1]-1 >= 0:
        left_location = [snake_head[0],snake_head[1]-1]
        if left_location not in snake:
            eligible_moves.append(left_location)

    return(eligible_moves)

def make_a_move(sleep_time, wait_times, number_of_nom_noms, number_of_bombs, number_of_caffeine_pills, level_0_nom_nom, level_1_nom_nom, level_2_nom_nom, display_on_lights_boolean, divisor):
    the_final_move = []
    secondary_final_move = []
    nom_nom_count = 0
    new_snake_1 = []
    biggest_value = 0
    secondary_biggest_value = 0
    new_snake_2 = []
    snake_head = snake[-1]
    equal_move_list = []
    equal_move_secondary_list = []

    eligible_moves = generate_eligible_moves(snake_head, snake) #generate all possible next moves

    if len(eligible_moves) == 0:
        raise no_more_eligible_moves
        return

    for appendage in snake: #copy snake
        new_snake_1.append(appendage)
    
    for chosen_move in eligible_moves: #for each possible move
        if chosen_move in nom_noms: #if the move picks up a nom-nom, give it weight using the level_0_nom_nom value set at the top
            nom_nom_count = nom_nom_count + level_0_nom_nom
        new_snake_1.append(chosen_move) #update the snake
        new_snake_1.remove(new_snake_1[0])
        snake_head_1 = new_snake_1[-1]
        eligible_moves_1 = generate_eligible_moves(snake_head_1,new_snake_1) #generate the new possible moves and repeat the process using level_1_nom_nom value

        for appendage in new_snake_1: #copy snake 2
            new_snake_2.append(appendage)
            
        if len(eligible_moves_1) > 0: #So here there is a big if/else that have the same commands, except the if generates the next level of snake, while the else goes directly to picking a move
            #These if/else checks are necessary because almost everything in the if loop is also in a for statement that assumes the len > 0
            for chosen_move_1 in eligible_moves_1: #if the move picks up a nom-nom, give it weight using the level_1_nom_nom value (which is less than the level_0 value because it's less immediate reward)
                if chosen_move_1 in nom_noms:
                    nom_nom_count = nom_nom_count + level_1_nom_nom

                new_snake_2.append(chosen_move_1) #update the snake
                new_snake_2.remove(new_snake_2[0])
                snake_head_2 = new_snake_2[-1]
                eligible_moves_2 = generate_eligible_moves(snake_head_2,new_snake_2)

                if len(eligible_moves_2) > 0: #Here's another instance of that if/else loop. The if will update the nom_nom_count while the else goes directly to picking a move.
                    #These if/else checks are necessary because almost everything in the if loop is also in a for statement that assumes the len > 0
                    for chosen_move_2 in eligible_moves_2:
                        if chosen_move_2 in nom_noms:
                            nom_nom_count = nom_nom_count + level_2_nom_nom

                        eligible_move_sum = len(eligible_moves)+len(eligible_moves_1)+len(eligible_moves_2)
                        the_sum_that_matters = eligible_move_sum + nom_nom_count
                        nom_nom_count = 0
                        #print(chosen_move, chosen_move_1, chosen_move_2, "the_sum_that_matters: ", the_sum_that_matters)

                        if the_sum_that_matters >= biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0:
                            if the_sum_that_matters > biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0:
                                biggest_value = the_sum_that_matters
                                the_final_move = chosen_move
                                equal_move_list = []
                            elif the_sum_that_matters == biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0 and chosen_move not in equal_move_list:
                                equal_move_list.append(chosen_move)
                                the_final_move = []
                                
                        if the_sum_that_matters >= secondary_biggest_value:
                            if the_sum_that_matters > secondary_biggest_value:
                                secondary_biggest_value = the_sum_that_matters
                                secondary_final_move = chosen_move
                                equal_move_secondary_list = []
                            elif the_sum_that_matters == secondary_biggest_value and chosen_move not in equal_move_secondary_list:
                                equal_move_secondary_list.append(chosen_move)
                else: #Remember, this is almost identical to the if statement
                        eligible_move_sum = len(eligible_moves)+len(eligible_moves_1)
                        the_sum_that_matters = eligible_move_sum + nom_nom_count
                        nom_nom_count = 0
                        if the_sum_that_matters >= biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0:
                            if the_sum_that_matters > biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0:
                                biggest_value = the_sum_that_matters
                                the_final_move = chosen_move
                                equal_move_list = []
                            elif the_sum_that_matters == biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0 and chosen_move not in equal_move_list:
                                equal_move_list.append(chosen_move)
                                the_final_move = []
                            
                        if the_sum_that_matters >= secondary_biggest_value:
                            if the_sum_that_matters > secondary_biggest_value:
                                secondary_biggest_value = the_sum_that_matters
                                secondary_final_move = chosen_move
                                equal_move_secondary_list = []
                            elif the_sum_that_matters == secondary_biggest_value and chosen_move not in equal_move_secondary_list:
                                equal_move_secondary_list.append(chosen_move)
        else: #Remember, this is almost identical to the if statement
            eligible_move_sum = len(eligible_moves)
            the_sum_that_matters = eligible_move_sum + nom_nom_count
            nom_nom_count = 0
            if the_sum_that_matters >= biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0:
                if the_sum_that_matters > biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0:
                    biggest_value = the_sum_that_matters
                    the_final_move = chosen_move
                    equal_move_list = []
                elif the_sum_that_matters == biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0 and chosen_move not in equal_move_list:
                    equal_move_list.append(chosen_move)
                    the_final_move = []
                    
            if the_sum_that_matters >= secondary_biggest_value:
                if the_sum_that_matters > secondary_biggest_value:
                    secondary_biggest_value = the_sum_that_matters
                    secondary_final_move = chosen_move
                    equal_move_secondary_list = []
                elif the_sum_that_matters == secondary_biggest_value and chosen_move not in equal_move_secondary_list:
                    equal_move_secondary_list.append(chosen_move)

        if len(equal_move_list) > 0:
            if len(equal_move_list) > 1:
                the_final_move = equal_move_list[random.randint(0,len(equal_move_list)-1)]
            else:
                the_final_move = equal_move_list[0]

    if the_final_move == [] and len(equal_move_list) == 0 and len(equal_move_secondary_list) > 0:
        if len(equal_move_secondary_list) > 1:
            the_final_move = equal_move_secondary_list[random.randint(0,len(equal_move_secondary_list)-1)]
        else:
            the_final_move = equal_move_secondary_list[0]
        
    if the_final_move == []: #if we keep failing this check: if the_sum_that_matters > biggest_value and len(eligible_moves_1) > 1 and len(eligible_moves_2) > 0
                                            #... then the_final_move will never get assigned. Secondary_final_move will be assigned in this case, and here we set it to the_final_move
        the_final_move = secondary_final_move

    return(the_final_move)
                     

class no_more_eligible_moves(Exception): pass
class secondary_final_move_exception(Exception): pass