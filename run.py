import random


board = [['0', '0', '0'],
         ['0', '0', '0'],
         ['0', '0', '0']]



def print_board(board):
    """
    Print the board game 
    """
    for row in board:
        print(" ".join(row))


def palce_ship(board):
    """
    Create the ships on the board
    """
    for i in range(3):
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        while board[row][col] != '0':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
        board[row][col] = 'S'


def get_guess():
    """
    Create the guesses function
    """
    while True:
        guess = input("Enter your (row column): ").split()
        if len(guess) != 2:
            print("Invalid input. Please enter a row and a column separated by space")
            continue
        try:
            row = int(guess[0])
            col = int(guess[1])
        except ValueError:
            print("Invalid input. Please enter numbers as integers")
            continue
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid input. Row and column must be between 1 and 3")
            continue
        return row - 1, col - 1


def battleship():
    """
    Create the game function
    """
    print("Start play BattleShip!")
    print_board(board)
    
    print("Ships placed!")
    print_board(board)

    turns = 0
    while True:
        print(f"Turn {turns + 1}:")
        print_board(board) 
        print()
        print("Player 1's turn:")
        guess_row, guess_col = get_guess()
        
        if board[guess_row][guess_col] == 'S':
            print("Congratulations! You hit a ship!")
            board[guess_row][guess_col] = 'X'
        else:
            print("Sorry, you missed!")

        
        print_board(board)
        print()
        
        if all(all(cell != 'S' for cell in row) for row in board):
            print("Player 1 wins!")
            break

        turns += 1

        print(f"Turn {turns + 1}:")
        print_board(board)
        print()
        print("Player 2's turn:")
        guess_row, guess_col = get_guess()
        
        if board[guess_row][guess_col] == 'S':
            print("Congratulations! You hit a ship!")
            board[guess_row][guess_col] = 'X'
        else:
            print("Sorry, you missed!")
        
        print_board(board)
        print()
        
        if all(all(cell != 'S' for cell in row) for row in board):
            print("Player 2 wins!")
            break
        
        turns += 1

# Start the game
battleship()


