class AyoGame:
    def __init__(self):
        # Your code here - initialize the board
        # Each of the 12 pits should start with 4 seeds
        # Player scores start at 0
        # Player 1 starts
        pass
    
    def display_board(self):
        # Your code here - show the current board state
        # Make it visually clear for players
        pass

# Test your initialization
game = AyoGame()
game.display_board()



















'''
        while True:
            # Create list of valid AI moves
            #valid_ai_pits = []
            f#or pit in range(6, 12):
                #if board[pit] > 0:
                    #valid_ai_pits.append(pit)
            
            # Randomly choose from valid pits
            if valid_ai_pits:
                player2 = [valid_ai_pits]
            else:
                print("Computer has no moves!")
                break
                
            print(f"You selected pit {player2}")
            if 6 <= player2 <= 11 and board[player2] > 0:
                seeds = board[player2]
                board[player2] = 0
                index = player2  # start at chosen pit

                while seeds > 0:
                    index = (index + 1) % 12  # move first
                    board[index] += 1
                    seeds -= 1
                    last_index = index  # track last pit
                    
                    
                break
                    
            else:
                print("Invalid move")
  ''' 