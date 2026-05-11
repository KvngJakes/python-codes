import random


PITS_PER_PLAYER = 6
TOTAL_PITS = 12
PLAYER = 1
COMPUTER = 2
CLOCKWISE = 1


def display_board(board, player_score, computer_score):
    print("\n" + "=" * 50)

    print("   ", end="")
    for i in range(11, 5, -1):
        print(f"[{i:2}]", end=" ")
    print()

    print("   ", end="")
    for i in range(11, 5, -1):
        print(f" {board[i]:2} ", end=" ")
    print("\n")

    print("   ", end="")
    for i in range(0, 6):
        print(f" {board[i]:2} ", end=" ")
    print()

    print("   ", end="")
    for i in range(0, 6):
        print(f"[{i:2}]", end=" ")
    print("\n")

    print(f"Player Score: {player_score}    Computer Score: {computer_score}")
    print("=" * 50)


def get_pits_for_player(player):
    if player == PLAYER:
        return range(0, 6)
    return range(6, 12)


def get_opponent_pits(player):
    if player == PLAYER:
        return range(6, 12)
    return range(0, 6)


def valid_moves(board, player):
    moves = []
    for pit in get_pits_for_player(player):
        if board[pit] > 0:
            moves.append(pit)
    return moves


def apply_move(board, pit, player):
    """Return a new board and the number of seeds captured by this move."""
    new_board = board.copy()
    seeds = new_board[pit]
    new_board[pit] = 0
    index = pit

    while seeds > 0:
        index = (index + CLOCKWISE) % TOTAL_PITS
        new_board[index] += 1
        seeds -= 1

    captured = capture_seeds(new_board, index, player)
    return new_board, captured


def capture_seeds(board, last_index, player):
    opponent_pits = get_opponent_pits(player)
    captured = 0

    if board[last_index] not in (1, 2):
        return 0

    index = last_index
    while index in opponent_pits and board[index] in (1, 2):
        captured += board[index]
        board[index] = 0
        index = (index - 1) % TOTAL_PITS

    return captured


def is_game_over(board):
    return sum(board[0:6]) == 0 or sum(board[6:12]) == 0


def finish_game(board, player_score, computer_score):
    player_score += sum(board[0:6])
    computer_score += sum(board[6:12])
    return player_score, computer_score


class Perceptron:
    def __init__(self, weights=None, bias=0.0, learning_rate=0.05):
        if weights is None:
            weights = [0.6, 0.2, 0.4, -0.3, 0.1]

        self.weights = weights
        self.bias = bias
        self.learning_rate = learning_rate

    def predict(self, features):
        total = self.bias
        for weight, feature in zip(self.weights, features):
            total += weight * feature
        return total

    def train(self, features, target, prediction):
        error = target - prediction

        for i in range(len(self.weights)):
            self.weights[i] += self.learning_rate * error * features[i]

        self.bias += self.learning_rate * error


def move_features(old_board, new_board, captured):
    computer_seeds = sum(new_board[6:12])
    player_seeds = sum(new_board[0:6])
    computer_moves = len(valid_moves(new_board, COMPUTER))
    player_moves = len(valid_moves(new_board, PLAYER))

    return [
        captured,
        computer_seeds - player_seeds,
        computer_moves - player_moves,
        len([pit for pit in range(0, 6) if new_board[pit] in (1, 2)]),
        max(new_board[6:12]),
    ]


def choose_perceptron_move(board, perceptron):
    best_pit = None
    best_score = None

    for pit in valid_moves(board, COMPUTER):
        new_board, captured = apply_move(board, pit, COMPUTER)
        features = move_features(board, new_board, captured)
        score = perceptron.predict(features)

        if best_score is None or score > best_score:
            best_score = score
            best_pit = pit

    return best_pit


def train_perceptron_from_result(perceptron, old_board, pit, final_score_change):
    new_board, captured = apply_move(old_board, pit, COMPUTER)
    features = move_features(old_board, new_board, captured)
    prediction = perceptron.predict(features)
    perceptron.train(features, final_score_change, prediction)


def ask_starting_player():
    while True:
        try:
            player = int(input("Press 1 for player and 2 for computer: "))
            if player in (PLAYER, COMPUTER):
                return player
        except ValueError:
            pass

        print("Enter 1 or 2.")


def ask_player_move(board):
    while True:
        try:
            pit = int(input("Choose a pit (0-5): "))
            if pit in valid_moves(board, PLAYER):
                return pit
        except ValueError:
            pass

        print("Invalid move. Choose a non-empty pit from 0 to 5.")


def play_game():
    board = [4] * TOTAL_PITS
    player_score = 0
    computer_score = 0
    current_player = ask_starting_player()
    perceptron = Perceptron()

    display_board(board, player_score, computer_score)

    last_computer_board = None
    last_computer_pit = None
    score_before_computer_move = 0

    while True:
        if current_player == PLAYER:
            pit = ask_player_move(board)
        else:
            last_computer_board = board.copy()
            score_before_computer_move = computer_score - player_score
            pit = choose_perceptron_move(board, perceptron)

            if pit is None:
                pit = random.choice(valid_moves(board, COMPUTER))

            last_computer_pit = pit
            print(f"Computer selects pit {pit}")

        board, captured = apply_move(board, pit, current_player)

        if current_player == PLAYER:
            player_score += captured
        else:
            computer_score += captured

        display_board(board, player_score, computer_score)

        if is_game_over(board):
            player_score, computer_score = finish_game(
                board,
                player_score,
                computer_score,
            )

            if last_computer_board is not None:
                final_score_change = computer_score - player_score
                improvement = final_score_change - score_before_computer_move
                train_perceptron_from_result(
                    perceptron,
                    last_computer_board,
                    last_computer_pit,
                    improvement,
                )

            print("Game Over!")
            print(f"Final Scores -> Player: {player_score}, Computer: {computer_score}")
            print(f"Perceptron weights after training: {perceptron.weights}")
            print(f"Perceptron bias after training: {perceptron.bias:.2f}")
            break

        current_player = COMPUTER if current_player == PLAYER else PLAYER


if __name__ == "__main__":
    play_game()
