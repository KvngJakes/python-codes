import random

def print_board(board, score1, score2):
    print("\nPlayer1 side:", board[0:6])
    print("Player2 side:", board[6:12])
    print(f"Scores -> Player1: {score1}, Player2: {score2}")


def get_move(board, current_player):
    while True:
        if current_player == 1:
            pit = int(input("Choose a pit (0-5): "))
            if 0 <= pit <= 5 and board[pit] > 0:
                return pit
        else:
            pit = int(input("Choose a pit (6-11): "))
            if 6 <= pit <= 11 and board[pit] > 0:
                return pit
        print("Invalid move")


def sow(board, pit):
    seeds = board[pit]
    board[pit] = 0
    index = pit

    while seeds > 0:
        index = (index + 1) % 12
        board[index] += 1
        seeds -= 1

    return index  # last_index


def capture(board, last_index, current_player):
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

    return captured


def is_starving(board, current_player):
    if current_player == 1:
        return sum(board[6:12]) == 0
    else:
        return sum(board[0:6]) == 0


def is_game_over(board):
    return sum(board[0:6]) == 0 or sum(board[6:12]) == 0


def play_game():
    board = [2] * 12
    score1 = 0
    score2 = 0

    current_player = int(input("Press 1 for Player1 and 2 for Player2: "))

    while True:

        print_board(board, score1, score2)

        pit = get_move(board, current_player)

        last_index = sow(board, pit)

        captured = capture(board, last_index, current_player)

        if is_starving(board, current_player):
            print("Illegal move! You cannot starve opponent.")
            continue

        if current_player == 1:
            score1 += captured
        else:
            score2 += captured

        print("Captured seeds:", captured)

        if is_game_over(board):
            score1 += sum(board[0:6])
            score2 += sum(board[6:12])
            break

        current_player = 2 if current_player == 1 else 1

    print("\nGame Over!")
    print("Final Board:", board)
    print(f"Final Scores -> Player1: {score1}, Player2: {score2}")

    if score1 > score2:
        print("Player 1 Wins!")
    elif score2 > score1:
        print("Player 2 Wins!")
    else:
        print("It's a Draw!")


# -------- REPLAY SYSTEM --------
while True:
    play_game()
    replay = input("\nPlay again? (y/n): ")
    if replay.lower() != 'y':
        break