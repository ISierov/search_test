PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def evaluate(board):
    '''This function evaluates the current state of the board and determines the outcome of the game.

    Parameters:
        board (list): A 3x3 array representing the board state with symbols.

    Returns:
        int:
            -1 if PLAYER_O has won.
            1 if PLAYER_X has won.
            0 if the game is a draw or still ongoing.
    '''
    # Function code here
    # Check rows
    for row in board:
        if row.count(PLAYER_X) == 3:
            return 1
        elif row.count(PLAYER_O) == 3:
            return -1

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == PLAYER_X:
            return 1
        elif board[0][col] == board[1][col] == board[2][col] == PLAYER_O:
            return -1

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == PLAYER_X or board[0][2] == board[1][1] == board[2][
        0] == PLAYER_X:
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == PLAYER_O or board[0][2] == board[1][1] == board[2][
        0] == PLAYER_O:
        return -1

    # Game is a draw
    return 0

def minimax(board, depth, alpha, beta, is_maximizing):
        '''Implements the Minimax algorithm with Alpha-Beta pruning to determine the optimal score for a given board state.

        Parameters:
            board (list): A 3x3 array representing the current board state with symbols.
            depth (int): The current depth of the recursion.
            alpha (int): The best score found so far for the maximizing player.
            beta (int): The best score found so far for the minimizing player.
            is_maximizing (bool): True if the current player is the maximizing player (Player X), False if the current player is the minimizing player (Player O).

        Returns:
            int:
                -1 if PLAYER_O has won.
                1 if PLAYER_X has won.
                0 if the game is a draw or still ongoing.
        '''
        # Function code here
        result = evaluate(board)

        if result != 0:
            return result

        if is_full(board):
            return 0

        if is_maximizing:
            max_eval = float('-inf')

            for move in get_empty_cells(board):
                row, col = move
                board[row][col] = PLAYER_X
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[row][col] = EMPTY

                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)

                if beta <= alpha:
                    break

            return max_eval
        else:
            min_eval = float('inf')

            for move in get_empty_cells(board):
                row, col = move
                board[row][col] = PLAYER_O
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[row][col] = EMPTY

                min_eval = min(min_eval, eval)
                beta = min(beta, eval)

                if beta <= alpha:
                    break

            return min_eval

def get_best_move(board):
    best_score = -10
    best_move = None
    for row, col in get_empty_cells(board):
        board[row][col] = PLAYER_X
        score = minimax(board, 0, float('-inf'), float('inf'), False)
        board[row][col] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def test_evaluate(func):

    board1 = [[PLAYER_O, PLAYER_O, PLAYER_X],
                  [EMPTY, PLAYER_X, EMPTY],
                  [EMPTY, EMPTY, PLAYER_X]]
    if func(board1) != evaluate(board1):
        print("Incorrect output of evaluate. (test 1)")

    board2 = [[PLAYER_O, PLAYER_O, PLAYER_O],
                  [EMPTY, PLAYER_X, EMPTY],
                  [EMPTY, EMPTY, PLAYER_X]]
    if func(board2) != evaluate(board2):
        print("Incorrect output of evaluate. (test 2)")

    board3 = [[PLAYER_X, PLAYER_O, PLAYER_O],
                  [EMPTY, PLAYER_X, EMPTY],
                  [EMPTY, EMPTY, PLAYER_X]]
    if func(board3) != evaluate(board3):
        print("Incorrect output of evaluate. (test 3)")

    return func

def test_best_move(func):
    board1 = [[PLAYER_O, PLAYER_O, PLAYER_X],
                  [EMPTY, PLAYER_X, EMPTY],
                  [EMPTY, EMPTY, PLAYER_X]]
    if func(board1) != get_best_move(board1):
        print("Incorrect output of get_best_move. (test 1)")

    board2 = [[PLAYER_O, PLAYER_O, PLAYER_O],
                  [EMPTY, PLAYER_X, EMPTY],
                  [EMPTY, EMPTY, PLAYER_X]]
    if func(board2) != get_best_move(board2):
        print("Incorrect output of get_best_move. (test 2)")

    board3 = [[PLAYER_X, PLAYER_O, PLAYER_O],
                  [EMPTY, PLAYER_X, EMPTY],
                  [EMPTY, EMPTY, PLAYER_X]]
    if func(board3) != get_best_move(board3):
        print("Incorrect output of get_best_move. (test 3)")

    return func

def test_minimax(func):
    board1 = [[PLAYER_O, PLAYER_O, PLAYER_X],
              [EMPTY, PLAYER_X, EMPTY],
              [EMPTY, EMPTY, PLAYER_X]]
    if func(board1, 0, float('-inf'), float('inf'), False) != minimax(board1, 0, float('-inf'), float('inf'), False):
        print("Incorrect output of get_best_move. (test 1)")

    board2 = [[PLAYER_O, PLAYER_O, PLAYER_O],
              [EMPTY, PLAYER_X, EMPTY],
              [EMPTY, EMPTY, PLAYER_X]]
    if func(board2, 0, float('-inf'), float('inf'), False) != minimax(board2, 0, float('-inf'), float('inf'), False):
        print("Incorrect output of get_best_move. (test 2)")

    board3 = [[PLAYER_X, PLAYER_O, PLAYER_O],
              [EMPTY, PLAYER_X, EMPTY],
              [EMPTY, EMPTY, PLAYER_X]]
    if func(board3, 0, float('-inf'), float('inf'), False) != minimax(board3, 0, float('-inf'), float('inf'), False):
        print("Incorrect output of get_best_move. (test 3)")

    return func









