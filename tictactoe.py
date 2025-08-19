# TicTacToe CLI Game - Complete Code

# Global variables to track game state
board = []  # This will hold our 9 positions
current_player = ""  # This will track whose turn it is

def new_game():
    """Start a new game by resetting the board and setting first player"""
    global board, current_player
    
    # Create empty board with 9 positions (0-8)
    # We'll use spaces " " for empty positions
    board = [" " for _ in range(9)]
    
    # X always starts first
    current_player = "X"
    
    print("New game started!")
    print("X goes first")
    display_board()

def display_board():
    """Show the current board state"""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\nPositions are numbered 0-8:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")
    print()

def play(position):
    """Make a move at the given position"""
    global board, current_player
    
    # Convert position to integer (in case it's a string)
    try:
        pos = int(position)
    except ValueError:
        print("Please enter a valid number (0-8)")
        return
    
    # Check if position is valid (0-8)
    if pos < 0 or pos > 8:
        print("Position must be between 0 and 8")
        return
    
    # Check if position is already taken
    if board[pos] != " ":
        print("That position is already taken!")
        return
    
    # Make the move
    board[pos] = current_player
    print(f"Player {current_player} played position {pos}")
    
    # Show updated board
    display_board()
    
    # Check for winner after the move
    winner = check_for_winner()
    if winner:
        if winner == "Tie":
            print("It's a tie! Game over.")
        else:
            print(f"Player {winner} wins! 🎉")
        print("Type 'new_game' to play again")
        return
    
    # Switch players only if game continues
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    
    print(f"It's now {current_player}'s turn")

def check_for_winner():
    """Check if there's a winner or if it's a tie"""
    global board
    
    # All possible winning combinations
    winning_combinations = [
        # Rows
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        # Columns
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        # Diagonals
        [0, 4, 8],
        [2, 4, 6]
    ]
    
    # Check each winning combination
    for combo in winning_combinations:
        # Get the values at these three positions
        a, b, c = combo[0], combo[1], combo[2]
        
        # If all three positions have the same player AND it's not empty
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  # Return the winning player (X or O)
    
    # Check for tie (board is full but no winner)
    if " " not in board:
        return "Tie"
    
    # No winner yet, game continues
    return None

# Test our game
if __name__ == "__main__":
    print("Welcome to TicTacToe!")
    print("Commands:")
    print("  play <position>  - Make a move (e.g., 'play 1')")
    print("  new_game        - Start a new game")
    print("  quit            - Exit the game")
    print()
    
    # Start the first game
    new_game()
    
    # Main game loop - this keeps the program running
    while True:
        try:
            # Get user input
            user_input = input("Enter command: ").strip().lower()
            
            # Handle quit command
            if user_input == "quit":
                print("Thanks for playing!")
                break
            
            # Handle new game command
            elif user_input == "new_game":
                new_game()
            
            # Handle play command
            elif user_input.startswith("play "):
                # Extract the position from "play 1" -> "1"
                parts = user_input.split()
                if len(parts) == 2:
                    position = parts[1]
                    play(position)
                else:
                    print("Usage: play <position> (e.g., 'play 1')")
            
            # Handle unknown commands
            else:
                print("Unknown command. Try 'play <position>', 'new_game', or 'quit'")
                
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nThanks for playing!")
            break