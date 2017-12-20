def test_dict():
	from startShow import startShow

	## Test tic tac toe

	dict = {
	'name': 'Big_Text_Scroller', 
	'input_string': 'WHOO PORTAL 2',
	'rainbow_bool': True,
	'text_color': 'Rainbow',
	'display_on_lights_boolean': 1, 
	'display_on_lights_train_boolean': 1, 
	'summary_print_bool': False, 
	'input_number_of_trains': 10, 
	'input_number_of_games': 10, 
	'x_win_weighting': 1, 
	'o_win_weighting': 1, 
	'sleep_time': 0.2, 
	'sleep_time_train': 0, 
	'divisor': 1,
	'divisor1': 1,	
	'divisor2': 1,
	'divisor3': 1,
	'divisor4': 1,
	'speed1': 1
	# 'number_of_bombs': 0,
	# 'number_of_nom_noms': 50
	}

	startShow(dict)

	print("Back in test dict")
