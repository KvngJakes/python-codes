last_index = 0
board = [4] * 12
score1 = 0
score2 = 0
direction = 1  # clockwise

def display_board(board, score1, score2):
    print("\n" + "="*50)

    # Top row (Computer side, reversed)
    print("   ", end="")
    for i in range(11, 5, -1):
        print(f"[{i:2}]", end=" ")
    print()

    print("   ", end="")
    for i in range(11, 5, -1):
        print(f" {board[i]:2} ", end=" ")
    print("\n")

    # Bottom row (Player side)
    print("   ", end="")
    for i in range(0, 6):
        print(f" {board[i]:2} ", end=" ")
    print()

    print("   ", end="")
    for i in range(0, 6):
        print(f"[{i:2}]", end=" ")
    print("\n")

    print(f"Player Score: {score1}    Computer Score: {score2}")
    print("="*40)


display_board(board, score1, score2)


#print("\nBoard:")
#print("Computer:", board[11:5:-1])
#print("Player:  ", board[0:6])
#print(f"Scores -> You: {score1} | AI: {score2}\n")

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

    # SOWING
    while seeds > 0:
        index = (index + direction) % 12
        sim_board[index] += 1
        seeds -= 1

    last_index = index

    # CAPTURE
    if player == 2:
        opponent_range = range(0, 6)
    else:
        opponent_range = range(6, 12)

    captured = 0

    # Only capture if last hole has 1 or 2
    if sim_board[last_index] in (1, 2):
        index = last_index
        while index in opponent_range and sim_board[index] in (1, 2):
            captured += sim_board[index]
            sim_board[index] = 0
            index = (index - 1) % 12

    return sim_board, captured


# -------- EVALUATION --------
def evaluate_board(board, gain):
    return gain + (sum(board[6:12]) - sum(board[0:6])) * 0.2


# -------- AI --------
def evaluate_3_moves(board):
    best_score = -999
    best_pit = None

    for ai_pit in range(6, 12):
        if board[ai_pit] == 0:
            continue

        board1, gain1 = simulate_move(board, ai_pit, 2)

        worst_case = 999

        for player_pit in range(0, 6):
            if board1[player_pit] == 0:
                continue

            board2, gain_player = simulate_move(board1, player_pit, 1)

            best_followup = -999

            for ai_pit2 in range(6, 12):
                if board2[ai_pit2] == 0:
                    continue

                board3, gain2 = simulate_move(board2, ai_pit2, 2)

                score = evaluate_board(board3, gain1 + gain2 - gain_player)

                if score > best_followup:
                    best_followup = score

            if best_followup < worst_case:
                worst_case = best_followup

        if worst_case > best_score:
            best_score = worst_case
            best_pit = ai_pit

    return best_pit


# -------- GAME LOOP --------
while True:

    if current_player == 1:
        while True:
            player1 = int(input("Choose a pit (0-5): "))
            if 0 <= player1 <= 5 and board[player1] > 0:
                seeds = board[player1]
                board[player1] = 0
                index = player1

                while seeds > 0:
                    index = (index + direction) % 12
                    board[index] += 1
                    seeds -= 1
                    last_index = index
                break
            else:
                print("Invalid move")

    else:
        player2 = evaluate_3_moves(board)
        print(f"Computer selects pit {player2}")

        seeds = board[player2]
        board[player2] = 0
        index = player2

        while seeds > 0:
            index = (index + direction) % 12
            board[index] += 1
            seeds -= 1
            last_index = index

    # -------- CAPTURE --------
    if current_player == 1:
        opponent_range = range(6, 12)
    else:
        opponent_range = range(0, 6)

    captured = 0

    if board[last_index] in (1, 2):
        index = last_index
        while index in opponent_range and board[index] in (1, 2):
            captured += board[index]
            board[index] = 0
            index = (index - 1) % 12

    if current_player == 1:
        score1 += captured
    else:
        score2 += captured

    display_board(board, score1, score2)
    #print(f'{board[0:6]}      {score1}')
    #print(f'{board[6:12]}      {score2}')

    # -------- GAME END --------
    if sum(board[0:6]) == 0 or sum(board[6:12]) == 0:
        score1 += sum(board[0:6])
        score2 += sum(board[6:12])

        print("Game Over!")
        print(f"Final Scores -> Player1: {score1}, Player2: {score2}")
        break

    # -------- TURN RULE --------
    current_player = 2 if current_player == 1 else 1