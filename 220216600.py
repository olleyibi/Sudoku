import numpy as np
import time

# sudoku = np.array([
#    [9, 0, 0, 1, 7, 0, 4, 0, 2],
#    [1, 6, 0, 0, 4, 0, 0, 9, 5],
#    [0, 0, 8, 0, 0, 3, 0, 0, 0],
#    [0, 1, 0, 9, 0, 0, 5, 7, 3],
#    [0, 4, 0, 0, 0, 0, 0, 2, 0],
#    [5, 8, 9, 0, 0, 7, 0, 1, 0],
#    [0, 0, 0, 4, 0, 0, 7, 0, 0],
#    [6, 7, 0, 0, 2, 0, 0, 5, 8],
#    [3, 0, 1, 0, 5, 8, 0, 0, 6]
# ])
input = 900170402160040095008003000010900573040000020589007010000400700670020058301058006


def input2arr(input: object) -> object:
    if len(str(input)) == 81:
        splits = np.array_split([int(i) for i in str(input)], 9)
        lists = []
        for i in splits:
            lists.append(list(i))
        return np.array(lists)
    else:
        return 'invalid input length'


def find_empty(sudoku_puzzle):
    # Find position in array that is not filled (position containing '0')
    for i in range(9):
        for j in range(9):
            if sudoku_puzzle[i][j] == 0:
                return i, j

    return None, None  # return when no space is empty


def valid(sudoku_puzzle, guess_value, row, column):
    row_values = sudoku_puzzle[row]

    # Checks if the guess value is in the row index
    if guess_value in row_values:
        print(f'Guess Value {guess_value} already found......')
        return False

    # Checks if column at the guessed position contains guessed value
    column_values = [sudoku_puzzle[i][column] for i in range(9)]
    if guess_value in column_values:
        print(f'Guess Value {guess_value} already found.....')
        return False

    # Get 3X3 matrix to validate the guessed value
    row_start = (row // 3) * 3
    column_start = (column // 3) * 3

    for x in range(row_start, row_start + 3):  # iterate through 3 rows
        for y in range(column_start, column_start + 3):  # iterate through 3 columns
            print(f'checking row {x}, column {y}................')
            if sudoku_puzzle[x][y] == guess_value:
                return False

    return True


def sudoku_solver(sudoku_puzzle):
    row, column = find_empty(sudoku_puzzle)  # choose somewhere on the board to make a guess

    # check if there are empty positions left
    if row is None:
        return True

    for guess_value in range(1, 10):
        # Check if guess is valid (True)
        if valid(sudoku_puzzle, guess_value, row, column):
            sudoku_puzzle[row][column] = guess_value  # insert guessed value into the puzzle

            # If sudoku puzzle is solved return true
            if sudoku_solver(sudoku_puzzle):
                return True

        # If Sudoku guess is wrong, backtrack and reset value to '0'
        sudoku_puzzle[row][column] = 0

    # Return False if puzzle is unsolvable
    return False


def main():
    start_time = time.time()
    try:
        begin = True
        while begin:
            sudoku = input2arr(input)
            if sudoku is not None:
                print(sudoku_solver(sudoku))
                print(sudoku)
                print(f'It took {time.time() - start_time} seconds to complete')
                begin = False
    except:
        print('Invalid Input')
        print(f'It took {time.time() - start_time} seconds to complete')
    finally:
        print('\n...................DONE!!!!.................\n'
              'Author: Ibidamola Daniel Olley\n\n'
              'This code is an application that solves a sudoku puzzle\n'
              'by filling up the empty slots in the puzzle identified by "0"\n'
              'It uses a backtrack recursive technique to solve the puzzle\n'
              'which allows it cross check the row and column and ensure there\n'
              'are no re-occuring numbers as well as the unit box of 9 slots. ')


main()

