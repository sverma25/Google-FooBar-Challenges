
board = [0 for i in range(64)]
moves_explored = []

def answer(src, dest):
    board[src] = 0
    count = 0
    moves = [src]

    while moves:
        move = moves[0]
        moves.remove(move)
        #print(move, moves)

        if move == dest:
            return board[move]
        elif move not in moves_explored:
            moves_explored.append(move)
            valid_moves = find_valid_moves(move, moves)
            moves.extend(valid_moves)
            update_steps_taken(move, valid_moves)

def find_valid_moves(src, moves):
    src_row = int(src/8)
    src_col = src - 8*src_row
    new_moves = []

    straight_left_codition = (src_col >= 2)
    straight_right_codition = (src_col <= 5)
    straight_up_codition = (src_row >= 2)
    straight_down_codition = (src_row <= 5)

    turn_left_codition = (src_col >= 1)
    turn_right_codition = (src_col <= 6)
    turn_up_codition = (src_row >= 1)
    turn_down_codition = (src_row <= 6)

    # For each valid move, set the counter up by one
    if (straight_up_codition and turn_left_codition): new_moves.append(src-17)
    if (straight_up_codition and turn_right_codition): new_moves.append(src-15)

    if (straight_right_codition and turn_up_codition): new_moves.append(src-6)
    if (straight_right_codition and turn_down_codition): new_moves.append(src+10)

    if (straight_down_codition and turn_left_codition): new_moves.append(src+15)
    if (straight_down_codition and turn_right_codition): new_moves.append(src+17)

    if (straight_left_codition and turn_up_codition): new_moves.append(src-10)
    if (straight_left_codition and turn_down_codition): new_moves.append(src+6)

    return list(filter(lambda x: x not in moves_explored, new_moves))

def update_steps_taken(src, valid_moves):
    for move in valid_moves: board[move] = board[src]+1


# print("ANS:", answer(0,63))
