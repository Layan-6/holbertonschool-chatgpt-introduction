#!/usr/bin/python3
def print_board(board):
    """
    Print the current state of the board.
    
    Parameters:
    board (list): 3x3 list representing the game board
    """
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

def check_winner(board):
    """
    Check if there's a winner on the board.
    
    Parameters:
    board (list): 3x3 list representing the game board
    
    Returns:
    bool: True if there's a winner, False otherwise
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Check if the board is completely filled.
    
    Parameters:
    board (list): 3x3 list representing the game board
    
    Returns:
    bool: True if board is full, False otherwise
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to run the Tic Tac Toe game.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Get valid row input
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                if row in [0, 1, 2]:
                    break
                else:
                    print("Invalid row! Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        # Get valid column input
        while True:
            try:
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if col in [0, 1, 2]:
                    break
                else:
                    print("Invalid column! Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        # Check if spot is available
        if board[row][col] == " ":
            board[row][col] = player
            
            # Check for winner
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!!")
                break
            
            # Check for tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
