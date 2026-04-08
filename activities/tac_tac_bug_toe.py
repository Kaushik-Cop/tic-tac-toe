'''A buggy Tic-Tac-Toe game that provides an opportunity to debug code by both reasoning about it and stepping through it in a debugger.
The program has a number of bugs that are introduced one at a time. The goal is to find and fix the bugs.
Ensure you step through this program in an IDE debugger to understand how the program works and to find the bugs.'''
#TODO Add pytest to show debugging
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    """Print the current state of the Tic-Tac-Toe board to the console."""
    for row in board:
     
        print('|'.join(row))
        print('-' * 5)


def is_win(player, board_snapshot=board):
    """Check rows, columns, and diagonals for win condition for a given player"""
    for i in range(3):
        if all (cell == player for cell in board_snapshot[i]):  # Rows
            return True
        if all (board_snapshot[j][i] == player for j in range(3)):  # Columns
            return True

    if board_snapshot[0][0] == board_snapshot[1][1] == board_snapshot[2][2] == player:
        return True
    if board_snapshot[0][2] == board_snapshot[1][1] == board_snapshot[2][0] == player:
        return True
    return False

def tally_wins(results):
    """Count the total number of wins from a list of boolean results.
    # Leveraging the fact that in Python: True = 1 and False = 0 
    # we can use sum() to count the number of wins by counting all Trues and Falses
    """
    return sum(results)


def main():
    """Run the main Tic-Tac-Toe game loop."""
    current_player = 'X'
    moves = 0
    results = [ ]

    while moves < 9:
        print_board()

        # Note that list comprehensions are more Pythonic, easier to read, and in recent versions of Python, faster.
        try:
            row, col = map(int,
                           input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
        except ValueError:
            print("Invalid input! Enter two numbers separated by space.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be between 0 and 2.")
            continue

        if board[row][col] == ' ':
            board[row][col] = current_player
            win = is_win(current_player)
            results.append(win)
            moves += 1

            if win:
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'  # Switch player

        else:
            print("Cell already occupied! Try again.")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")


if __name__ == "__main__":
    main()
