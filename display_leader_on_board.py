def display_leader_on_board(board):
	white_score = 0
	black_score = 0
	for i in range(8):
		for j in range(8):
			if board[i,j] == 1:
				white_score += 1
			if board[i,j] == 2:
				black_score += 1
	return white_score - black_score