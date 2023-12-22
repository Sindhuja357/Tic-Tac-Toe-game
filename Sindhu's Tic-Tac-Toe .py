# Initialize the game board as a 3x3 grid
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board():
    print("  0   1   2")
    for i, row in enumerate(board):
        print(i, end=' ')
        for cell in row:
            print(f"| {cell} ", end='')
        print("\n  -----------")

# Function to check if a player has won
def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to get user input for a move
def get_user_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))

            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main game loop
current_player = 'X'
while True:
    print_board()
    row, col = get_user_move(current_player)

    # Set the chosen cell to the current player's symbol
    board[row][col] = current_player

    # Check for a win or a draw
    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins! Congratulations!")
        break
    elif all(cell != ' ' for row in board for cell in row):
        print_board()
        print("It's a draw!")
        break

    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'
