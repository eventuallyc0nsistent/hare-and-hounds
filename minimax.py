import sys


def mini_max(board, player):
    return max_move(board, player)


def max_move(board, player):
    if game_ended(board, player):
        return eval_game_state(board, player)
    else:
        best_move = []
        moves = next_moves(board, player)
        sys.exit(0)
        for move in moves:
            board.setHare(move)
            min_move(board, player)


def eval_game_state(board, player):
    if player == 'hare':
        print 'Hare'


def game_ended(board, player):
    if player == 'hare':

        if board.hare[0] == (1, 0):
            """ Check if the hare is at the goal state tuple (1, 0) """
            print '-----GAMEOVER-----'
            return True
        else:
            """ Compare the sets for hare and hounds and if next move contains all hounds then return True """
            hounds = board.hounds
            nextmoves_hare = next_moves(board, player)
            if len(set(hounds) & set(nextmoves_hare)) == 3 and len(nextmoves_hare) == 3:
                print '-----GAMEOVER-----'
                return True
            else:
                return False


def next_moves(board, player):
    moves = []
    if player == 'hare':
        hare = board.hare[0]
        # ==================
        #  Next hare moves
        # ==================
        dtopleft = (hare[0] - 1, hare[1] - 1)
        dtopright = (hare[0] - 1, hare[1] + 1)
        dbotleft = (hare[0] + 1, hare[1] - 1)
        dbotright = (hare[0] + 1, hare[1] + 1)
        top = (hare[0] - 1, hare[1])
        bottom = (hare[0] + 1, hare[1])
        left = (hare[0], hare[1] - 1)
        right = (hare[0], hare[1] + 1)
        """
        From the moves the hare can perform
        Check if the move is legal for the board
        And the move is not where the hound is right now
        Append and return the list of moves
        """
        hare_moves = [dtopleft, dtopright, dbotright, dbotleft, top, bottom, left, right]
        for move in hare_moves:
            if move in board.legalMoves:
                moves.append(move)
        return moves

    else:
        hound_moves = board.hounds
        print "hound moves"


def min_move(board, player):
    best_move = []
    moves = next_moves(board, player)
    for move in moves:
        max_move(board, player)
