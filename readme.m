Code Description
* The input2arr Function:
    - This takes in either a string or integer numbers and convert it to an 2D array
    - The array consists of 9 list containing 9 elements each


* The find_next Function:
    - This searches for the next position in column and row index that is yet to be solved
    - The unsolved index positions are represented by an integer '0'
    - Depending in its finding in the search, a tuple of (row, col) or (None, None) if there is none will be returned


* The valid function:
    - This determines whether the value guessed at the (row,col) position in the sudoku puzzle is a valid result
    - It returns a boolean output of True or False depending on the outcome


* The sudoku_solver:
    - This solves the sudoku puzzle by using a backtracking method
    - It takes in the puzzle which is an array of of lists that contains the reapective rows of the sudoku puzzle
    - It updates the sudoku puzzle with the correct solution and returns a True or False value depending on its ability to reach a solution
    - It takes the following steps to solve the puzzle:
       + It selects a row, column index position to make a guess (select a position containing value '0')
       + Provided there happens to be no available position, it signifies the end as only valid inputs were allowed
       + On the otherhand, if there is a place to put a number, then the '0' position is replaced with a guessed value between 1 and 9
       + Then it validates the guess by calling the "valid function"
       + If this is a valid guess, then the sudoku puzzle is updated with the value at the selected position
       + Then the sudoku_solver is called recursively
       + Given the guess is not valid, the the the processed is backtracked to try guessing a new number
       + Provided all the guessed numbers are invalid, then the sudoku puzzle is assumed UNSOLVABLE!! and no updates will be made on the sudoku puzzle array



How to run
    - Provide input of only numeric elements of either integer or string format
    - Ensure that the input lengthe is exactly 81
    - All empty positions will be identified as '0' in the input
    - Click run on the compiler to get an output