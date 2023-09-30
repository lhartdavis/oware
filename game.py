class Game:

    def __init__(self):
        """player 0 controls first 6 cells and player 1 the following 6"""
        self.board = [4]*12
        self.scores = [0, 0]
        self.next_player = 0

    def play(self, move: int):
        """Play a move for the current player."""
        seeds = self.board[move]
        self.board[move] = 0

        idx = move
        while seeds > 0:
            idx = (idx + 1) % 12
            self.board[idx] += 1
            seeds -= 1

        # Capturing
        while 6 <= idx <= 11 and (self.board[idx] == 2 or self.board[idx] == 3):
            self.scores[self.next_player] += self.board[idx]
            self.board[idx] = 0
            idx -= 1

        # Switch player
        self.next_player = 1 - self.next_player

    def is_legal(self, move: int) -> bool:
        """Check if a move is legal for the current player."""
        if self.next_player == 0 and 0 <= move <= 5 or self.next_player == 1 and 6 <= move <= 11:
            return self.board[move] > 0
        return False

    def get_all_legal_moves_for_next_player(self):
        """Returns all legal moves for the current player."""
        if self.next_player == 0:
            return [i for i in range(6) if self.board[i] > 0]
        else:
            return [i for i in range(6, 12) if self.board[i] > 0]

    def print_board(self):
        """Print the game board."""
        print(' '.join(str(x) for x in self.board[6:12][::-1]))
        print(' '.join(str(x) for x in self.board[:6]))

    def is_over(self):
        """Check if the game is over."""
        return all(cell == 0 for cell in self.board[:6]) or all(cell == 0 for cell in self.board[6:12])


if __name__ == "__main__":
	game = Game()

	while not game.is_over():
		game.print_board()
		print(game.get_all_legal_moves_for_next_player())
		game.play(int(input(f"player {game.next_player}, please enter your move : ")))
