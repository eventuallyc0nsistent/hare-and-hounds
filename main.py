from minimax import mini_max


class Board:

    def __init__(self):
        self.hounds = [1, 5, 11]
        self.hare = [9]
        self.blank_spaces = [0, 4, 10, 14]
        self.player = ''
        self.board = self.printboard(self.hounds, self.hare)

    def printboard(self, hounds, hare):
        """ Print the board"""
        self.board = ['-' for i in range(0, 15)]

        for i in range(0, 15, 5):
            for j in range(0, 5):
                if (j + i) in self.blank_spaces:
                    print ' ',
                else:
                    if (j + i) in self.hounds:
                        print 'X',
                    elif (j + i) in self.hare:
                        print '0',
                    else:
                        print '-',
            print '\n'

    def selectPlayer(self):
        """ Select player as hound or hare"""
        player = raw_input('Hound or hare ?')
        self.setPlayer(player)

    def setPlayer(self, player):
        """ Set player as hound or hare"""
        self.player = player

    def getPlayer(self):
        return self.player

    def getHounds(self):
        return self.hounds

    def getHare(self):
        return self.hare

    def setHare(self, hare):
        self.hare = hare

    def setHounds(self, hounds):
        self.hounds = hounds

    def getMoves(self, board, player):
        moves = []
        if player == 'hare':
            hare = board.getHare()

            if hare[0] - 5 - 1 < 5 or hare[0] - 5 - 1 < 10:
                print hare[0] - 5 - 1

            for i in board.blank_spaces:
                if i in moves and i not in range(0, 15):
                    moves.remove(i)
            print moves
            board.printboard(board.getHounds(), board.getHare())


board = Board()
board.selectPlayer()

if board.getPlayer() == 'hare':
    minimax = mini_max(board, board.getPlayer())
