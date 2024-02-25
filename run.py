import random


HIDDEN_BOARD = [['0' for x in range(3)] for x in range(3)]
GUESS_BOARD = [['0' for x in range(3)] for x in range(3)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship(HIDDEN_BOARD):
    for i in range(3):
        row = random.randint(0, len(HIDDEN_BOARD) - 1)
        col = random.randint(0, len(HIDDEN_BOARD[0]) - 1)
        while HIDDEN_BOARD[row][col] != '0':
            row = random.randint(0, len(HIDDEN_BOARD) - 1)
            col = random.randint(0, len(HIDDEN_BOARD[0]) - 1)
        HIDDEN_BOARD[row][col] = 'S'

def get_guess():
    while True:
        guess = input("Enter your (row column): ").split()
        if len(guess) != 2:
            print("Invalid input. Please enter a row and a column separated by space")
            continue
        try:
            row = int(guess[0]) 
            col = int(guess[1]) 
            if row < 0 or row > 3 or col < 0 or col > 3:
                raise ValueError
        except ValueError:
            print(f"Invalid input. Please enter numbers as integers")
            continue
        return row -1, col -1
    
    
def check_win(GUESS_BOARD):
    all(all(cell != 'S' for cell in row) for row in GUESS_BOARD)

def battleship():
    print("Start play BattleShip!")
    print("Ships placed!")
    place_ship(GUESS_BOARD)
    
    turns = 4
    while True:
        print_board(HIDDEN_BOARD)
        print("Player's 1 turn:")
        guess_row, guess_col = get_guess()
        if GUESS_BOARD[guess_row][guess_col] == 'S':
            print("Congratulations! You hit a ship!")
            HIDDEN_BOARD[guess_row][guess_col] = 'X'
        else:
            print("Sorry, you missed!")

        if check_win(GUESS_BOARD):
            print('Congratulations! You sank all the ships!')
            break
        
        turns -= 1
        if turns == 0:
            print('Game Over! Sorry you dont have any more guesses.')
            break
            
    

battleship()
