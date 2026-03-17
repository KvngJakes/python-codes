import random
last_index = 0
board = [4] * 12
score1 = 0
score2 = 0

print(f'FULL BOARD: {board}')
print(board[0:6])
print(board[6:12])

current_player = int(input("Press 1 for player1 and 2 for player2: "))

while True:
    
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
                
    else:  
        best_score_ai = -1
        best_pit_ai = None
        
        
        for pit in range(6, 12):
            if board[pit] > 0: 
                sim_board = board.copy()
                sim_score2 = score2  
                
                
                seeds = sim_board[pit]
                sim_board[pit] = 0
                index = pit
                
                
                while seeds > 0:
                    index = (index + 1) % 12
                    sim_board[index] += 1
                    seeds -= 1
                    sim_last_index = index
                
                
                captured = 0
                opponent_range = range(0, 6)
                index = sim_last_index
                
                while index in opponent_range and sim_board[index] in (2, 3):
                    captured += sim_board[index]
                    sim_board[index] = 0
                    index -= 1
                
                sim_score2 += captured
                
                
                
                move_score = sim_score2
                
                
                if move_score > best_score_ai:
                    best_score_ai = move_score
                    best_pit_ai = pit
        
        
        if best_pit_ai is not None:
            player2 = best_pit_ai
            print(f"Computer selects pit {player2}")
            
            if 6 <= player2 <= 11 and board[player2] > 0:
                seeds = board[player2]
                board[player2] = 0
                index = player2
                
                while seeds > 0:
                    index = (index + 1) % 12
                    board[index] += 1
                    seeds -= 1
                    last_index = index

             
    

    # ---------------->>>> CAPTURE (BEFORE SWITCHING PLAYER)

    if current_player == 1:
        opponent_range = range(6, 12)
    else:
        opponent_range = range(0, 6)

    index = last_index
    captured = 0

    while index in opponent_range and board[index] in (2, 3):
        captured += board[index]
        board[index] = 0
        index -= 1 

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

        break  # <-- This break ends the game loop

    # ----------- NOW SWITCH PLAYER -----------
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1 


