import random

last_index = 0

board = [4] * 12

# scores for players
score1 = 0
score2 = 0


def simulate_move(sim_board, pit, player, s1, s2):

    sim_board = sim_board.copy()  

    seeds = sim_board[pit]        
    sim_board[pit] = 0
    index = pit

    
    while seeds > 0:
        index = (index + 1) % 12
        sim_board[index] += 1
        seeds -= 1
        last = index

    
    if player == 1:
        opponent_range = range(6,12)
    else:
        opponent_range = range(0,6)

    captured = 0
    index = last

    
    while index in opponent_range and sim_board[index] in (2,3):
        captured += sim_board[index]
        sim_board[index] = 0
        index = (index - 1) % 12

    
    if player == 1:
        s1 += captured
    else:
        s2 += captured

    return sim_board, s1, s2


# ---------------- SEARCH FUNCTION ----------------
def search_best_move(board, score1, score2):

    best_score = -9999
    best_pit = None

    # -------- FIRST MOVE --------
    for ai_pit in range(6,12):

        if board[ai_pit] == 0:
            continue

        b1, s1, s2 = simulate_move(board, ai_pit, 2, score1, score2)

        worst_for_ai = 9999

        # -------- PLAYER RESPONSE --------
        for player_pit in range(0,6):

            if b1[player_pit] == 0:
                continue

            b2, ps1, ps2 = simulate_move(b1, player_pit, 1, s1, s2)

            best_second_ai = -9999

            # -------- SECOND MOVE --------
            for ai_pit2 in range(6,12):

                if b2[ai_pit2] == 0:
                    continue

                b3, s1_final, s2_final = simulate_move(b2, ai_pit2, 2, ps1, ps2)

                
                score = s2_final - s1_final

                
                if score > best_second_ai:
                    best_second_ai = score

            
            if best_second_ai < worst_for_ai:
                worst_for_ai = best_second_ai

           
            if worst_for_ai < best_score:
                break

        if worst_for_ai > best_score:
            best_score = worst_for_ai
            best_pit = ai_pit

    return best_pit


# ------------- INITIAL BOARD PRINT -------------
print(f'FULL BOARD: {board}')
print(board[0:6])
print(board[6:12])


# choose starting player
current_player = int(input("Press 1 for player1 and 2 for player2: "))


# ---------------- MAIN GAME LOOP ----------------
while True:

    # -------- PLAYER TURN --------
    if current_player == 1:

        while True:

            player1 = int(input("Choose a pit (0-5):"))
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



    # -------- COMPUTER TURN --------
    else:

        player2 = search_best_move(board, score1, score2)

        print(f"Computer selects pit {player2}")

        seeds = board[player2]
        board[player2] = 0
        index = player2

        while seeds > 0:

            index = (index + 1) % 12
            board[index] += 1
            seeds -= 1
            last_index = index



    # -------- CAPTURE LOGIC --------
    if current_player == 1:
        opponent_range = range(6,12)
    else:
        opponent_range = range(0,6)

    index = last_index
    captured = 0

    while index in opponent_range and board[index] in (2,3):

        captured += board[index]
        board[index] = 0
        index = (index - 1) % 12

    if current_player == 1:
        score1 += captured
    else:
        score2 += captured


    print(f"Captured seeds: {captured}")
    print(f"Scores -> Player1: {score1}, Player2: {score2}")
    print(f"Board after capture: {board}")


    # -------- GAME END CHECK --------
    if sum(board[0:6]) == 0 or sum(board[6:12]) == 0:

        score1 += sum(board[0:6])
        score2 += sum(board[6:12])

        print("Game Over!")
        print(f"Final Scores -> Player1: {score1}, Player2: {score2}")

        if score1 > score2:
            print("Player 1 Wins!")
        elif score2 > score1:
            print("Player 2 Wins!")
        else:
            print("It's a Draw!")

        break


    # -------- SWITCH PLAYER --------
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1