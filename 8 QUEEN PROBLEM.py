def print_board(board):
    for row in board:
        print(" ".join(row))
def is_safe(board, row, col):
    # Check the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # Check upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    # Check upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < 8:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True
def solve(board, row):
    if row == 8:
        return True
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            if solve(board, row + 1):
                return True
            # Backtrack
            board[row][col] = '.'
    return False

# Main program
board = [['.' for _ in range(8)] for _ in range(8)]
if solve(board, 0):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists")
