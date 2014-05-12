from minimax import mini_max


class Board:

    def __init__(self):
        self.hounds = [(0, 1), (1, 1), (2, 1)]
        self.hare = [(1, 0)]
        self.legalMoves = self.legalMoves()

    def legalMoves(self):
        """
        Legal moves are moves that are present of the board
        i.e. moves that can't exist on the board in the tuple
        """
        legalMoves = []
        blanks = [(0, 0), (2, 0), (0, 4), (2, 4)]
        for i in range(0, 3):
            for j in range(0, 5):
                if (i, j) not in blanks:
                    legalMoves.append((i, j))
        return legalMoves

if __name__ == "__main__":
    board = Board()
    mini_max(board, 'hare')
