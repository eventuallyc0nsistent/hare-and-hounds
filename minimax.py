def mini_max(board, player):
    return max_move(board, player)


def max_move(board, player):
    if game_ended(board, player):
        return eval_game_state(board, player)
    else:
        best_move = []
        moves = next_moves(board, player)
        for move in moves:
            print move


def game_ended(board, player):
    if player == 'hare':
        hounds = board.getHounds()
        hare = board.getHare()

        # Compare the sets for hare and hounds and if next move contains all hounds then return True
        if len(set(hounds) & set(next_moves(board, player))) == 3:
            return True
        else:
            return False


def next_moves(board, player):
    moves = []
    # @todo : the diagonal moves need to be restricted to problemset in Question
    if player == 'hare':
        hare = board.getHare()[0]
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

        haremoves = [dtopleft, dtopright, dbotright, dbotleft, top, bottom, left, right]
        for move in haremoves:
            if move in board.legalMoves and move not in board.hounds:
                moves.append(move)
        return moves
