from minimax import mini_max


class Board:

    def __init__(self):
        self.hounds = [(0, 1), (1, 0), (2, 1)]
        self.hare = [(0, 2)]
        self.legalMoves = self.legalMoves()

    def legalMoves(self):
        """
        Legal moves are moves that are present of the board
        i.e. removing the moves from 
        """
        legalMoves = []
        blanks = [(0, 0), (2, 0), (0, 4), (2, 4)]
        for i in range(0, 3):
            for j in range(0, 5):
                if (i, j) not in blanks:
                    legalMoves.append((i, j))
        return legalMoves

    def getHounds(self):
        return self.hounds

    def getHare(self):
        return self.hare

    def setHounds(self, hounds):
        self.hounds = hounds

    def setHare(self, hare):
        self.hare = hare

if __name__ == "__main__":
    board = Board()
    mini_max(board, 'hare')
