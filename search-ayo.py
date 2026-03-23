last_index = 0
board = [4] * 12
score1 = 0
score2 = 0

print(f'FULL BOARD: {board}')
print(board[0:6])
print(board[6:12])

# -------- INPUT --------
current_player = int(input("Press 1 for player1 and 2 for player2: "))
while current_player not in [1, 2]:
    current_player = int(input("Enter 1 or 2: "))


# -------- SIMULATE MOVE --------
def simulate_move(board, pit, player):
    sim_board = board.copy()
    seeds = sim_board[pit]
    sim_board[pit] = 0
    index = pit

    while seeds > 0:
        index = (index + 1) % 12
        sim_board[index] += 1
        seeds -= 1

    last_index = index

    if player == 2:
        opponent_range = range(0, 6)
    else:
        opponent_range = range(6, 12)

    captured = 0
    index = last_index

    while index in opponent_range and sim_board[index] in (2, 3):
        captured += sim_board[index]
        sim_board[index] = 0
        index = (index - 1) % 12

    # Prevent illegal capture
    if player == 2 and sum(sim_board[0:6]) == 0:
        captured = 0
    elif player == 1 and sum(sim_board[6:12]) == 0:
        captured = 0

    return sim_board, captured


# -------- EVALUATION FUNCTION --------
def evaluate_board(board, score_gain):
    ai_side = sum(board[6:12])
    player_side = sum(board[0:6])
    return score_gain + (ai_side - player_side) * 0.2


# -------- 3-MOVE LOOKAHEAD AI --------
def evaluate_3_moves(board):
    best_score = -999
    best_pit = None

    for ai_pit in range(6, 12):
        if board[ai_pit] == 0:
            continue

        board1, score1 = simulate_move(board, ai_pit, 2)

        alpha = -999
        beta = 999

        worst_case = 999

        # PLAYER MOVE
        for player_pit in range(0, 6):
            if board1[player_pit] == 0:
                continue

            board2, score_player = simulate_move(board1, player_pit, 1)

            best_followup = -999

            # AI SECOND MOVE
            for ai_pit2 in range(6, 12):
                if board2[ai_pit2] == 0:
                    continue

                board3, score2 = simulate_move(board2, ai_pit2, 2)

                total = evaluate_board(
                    board3,
                    score1 + score2 - score_player
                )

                if total > best_followup:
                    best_followup = total

                # Alpha-Beta pruning
                if best_followup > alpha:
                    alpha = best_followup

                if alpha >= beta:
                    break

            if best_followup < worst_case:
                worst_case = best_followup

            if worst_case < beta:
                beta = worst_case

            if beta <= alpha:
                break

        if worst_case > best_score:
            best_score = worst_case
            best_pit = ai_pit

    return best_pit


# -------- MAIN GAME LOOP --------
while True:

    if current_player == 1:
        while True:
            player1 = int(input("Choose a pit (0-5): "))
            print(f"You selected pit {player1}")

            if 0 <= player1 <= 5 and board[player1] > 0:
                seeds = board[player1]
                board[player1] = 0
                index = player1

                while seeds > 0:
                    index = (index + 1) % 12
                    board[index] += 1
                    seeds -= 1
                    last_index = index

                break
            else:
                print("Invalid move")

    else:
        player2 = evaluate_3_moves(board)

        if player2 is not None:
            print(f"Computer selects pit {player2}")

            seeds = board[player2]
            board[player2] = 0
            index = player2

            while seeds > 0:
                index = (index + 1) % 12
                board[index] += 1
                seeds -= 1
                last_index = index

    # -------- CAPTURE --------
    if current_player == 1:
        opponent_range = range(6, 12)
    else:
        opponent_range = range(0, 6)

    index = last_index
    captured = 0

    while index in opponent_range and board[index] in (2, 3):
        captured += board[index]
        board[index] = 0
        index = (index - 1) % 12

    # Prevent illegal capture
    if current_player == 1 and sum(board[6:12]) == 0:
        captured = 0
    elif current_player == 2 and sum(board[0:6]) == 0:
        captured = 0

    if current_player == 1:
        score1 += captured
    else:
        score2 += captured

    print(f"Captured seeds: {captured}")
    print(f"Scores -> Player1: {score1}, Player2: {score2}")
    print(f"Board: {board}")

    # -------- GAME END --------
    if sum(board[0:6]) == 0 or sum(board[6:12]) == 0:
        score1 += sum(board[0:6])
        score2 += sum(board[6:12])

        print("Game Over!")
        print(f"Final Scores -> Player1: {score1}, Player2: {score2}")

        if score1 > score2:
            print("Player 1 Wins!")
        elif score2 > score1:
            print("Computer Wins!")
        else:
            print("It's a Draw!")

        break

    # -------- SWITCH PLAYER --------
    current_player = 2 if current_player == 1 else 1