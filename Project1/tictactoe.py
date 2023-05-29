"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = sum(row.count(X) for row in board)
    num_o = sum(row.count(O) for row in board)

    if num_x == num_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                action_set.add((i, j))

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    # Check that the specified cell is empty
    if board[i][j] is not None:
        raise Exception("Invalid action")
    # Copy the board to avoid modifying the original
    new_board = [row.copy() for row in board]
    # Fill the specified cell with the current player's symbol
    new_board[i][j] = player(board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontal
    for row in board:
        if all([ch == X for ch in row]):
            return X
        elif all([ch == O for ch in row]):
            return O

    # Check vertical
    for col in range(len(board[0])):
        if all([board[row][col] == X for row in range(len(board))]):
            return X
        elif all([board[row][col] == O for row in range(len(board))]):
            return O

    # Check diagonals
    if all([board[i][i] == X for i in range(len(board))]):
        return X
    elif all([board[i][i] == O for i in range(len(board))]):
        return O

    if all([board[i][len(board) - i - 1] == X for i in range(len(board))]):
        return X
    elif all([board[i][len(board) - i - 1] == O for i in range(len(board))]):
        return O

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        if all([ch == X for ch in row]) or all([ch == O for ch in row]):
            return True

    # Check vertical
    for col in range(len(board[0])):
        if all([board[row][col] == X for row in range(len(board))]) or all(
                [board[row][col] == O for row in range(len(board))]):
            return True

    # Check diagonals
    if all([board[i][i] == X for i in range(len(board))]) or all([board[i][i] == O for i in range(len(board))]):
        return True

    if all([board[i][len(board) - i - 1] == X for i in range(len(board))]) or all(
            [board[i][len(board) - i - 1] == O for i in range(len(board))]):
        return True

    # Check tie
    if all([ch is not None for row in board for ch in row]):
        return True

    # Game is not over
    return False


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    board[row][col]
    """
    for row in board:
        if all([ch == X for ch in row]):
            return 1
        elif all([ch == O for ch in row]):
            return -1

    # Check vertical
    for col in range(len(board[0])):
        if all([board[row][col] == X for row in range(len(board))]):
            return 1
        elif all([board[row][col] == O for row in range(len(board))]):
            return -1

    # Check diagonals
    if all([board[i][i] == X for i in range(len(board))]):
        return 1
    elif all([board[i][i] == O for i in range(len(board))]):
        return -1

    if all([board[i][len(board) - i - 1] == X for i in range(len(board))]):
        return 1
    elif all([board[i][len(board) - i - 1] == O for i in range(len(board))]):
        return -1

    # No winner
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    # Define helper function to calculate the minimax score of a given board
    def minimax_score(board, maximizing_player):
        if terminal(board):
            return score(board)

        if maximizing_player:
            best_score = float('-inf')

            for action in actions(board):
                result_board = result(board, action)
                action_score = minimax_score(result_board, False)
                best_score = max(best_score, action_score)

            return best_score
        else:
            best_score = float('inf')

            for action in actions(board):
                result_board = result(board, action)
                action_score = minimax_score(result_board, True)
                best_score = min(best_score, action_score)

            return best_score

    # Calculate the optimal action
    best_action = None
    best_score = None

    for action in actions(board):
        result_board = result(board, action)
        action_score = minimax_score(result_board, current_player == X)

        if best_score is None or (current_player == X and action_score > best_score) or \
                (current_player == O and action_score < best_score):
            best_score = action_score
            best_action = action

    return best_action
