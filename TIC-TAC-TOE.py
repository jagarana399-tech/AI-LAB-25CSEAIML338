def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
# Function to check the winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Main program
board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"
for turn in range(9):
    print_board(board)
    print("Player", player)
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if board[row][col] != " ":
        print("Cell already occupied! Try again.")
        continue
    board[row][col] = player
    if check_winner(board):
        print_board(board)
        print("Player", player, "wins!")
        break
    player = "O" if player == "X" else "X"
else:
    print_board(board)
    print("It's a draw!")
