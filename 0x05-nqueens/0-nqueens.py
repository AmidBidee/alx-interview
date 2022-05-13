#!/usr/bin/python3
"""
N queens

Usage: nqueens N
    - If the user called the program with the wrong number
      of arguments, print Usage: nqueens N, followed by
      a new line, and exit with the status 1

Where N must be an integer greater or equal to 4
    - if N is not an integer, print N must be a number
      followed by a new line, and exit with the status 1
    - If N is smaller than 4, print N must be at least 4
    followed by a new line, and exit with the status 1

The program should print every possible solution to the problem
    - One solution per line
    - Format: see example
    - You dont have to print the solutions in a specific order

"""


def validateAndReturnArg(args: list) -> int:
    """
    checks if arguments meet required lenght, type and size

    Arg:
        args [list]: list of command line arguments

    Return:
        n (int)
    """
    if len(args) > 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        n = int(args.pop(1))
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    return n


def initializeBoard():
    """
    returns an empty board filled with zeros
    """
    board = [[0] * N for i in range(N)]
    return board


def isSafe(board, row, col):
    """
    checks board
    """

    # Check this row on left side
    for i in range(col):
        if (board[row][i]):
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i = row
    j = col
    while j >= 0 and i < 4:
        if(board[i][j]):
            return False
        i = i + 1
        j = j - 1

    return True


def nqueens(n: int, board: list, result: list, col: int) -> bool:
    """
    nqueens puzzle solution
    """
    if (col == n):
        for row in range(n):
            for col in range(n):
                print(board[row][col], end=" ")
                if board[row][col] == 1:
                    result.insert(col, [row, col])
            print()
        result.sort()
        print(result)
        print()
        result.clear()
        return True

    res = False
    for i in range(n):
        if (isSafe(board, i, col)):
            board[i][col] = 1

            res = nqueens(n, board, result, col + 1) or res

            board[i][col] = 0

    return res


if __name__ == '__main__':
    import sys

    args = sys.argv
    N = validateAndReturnArg(args)
    board = initializeBoard()
    result = []

    nqueens(N, board, result, 0)
