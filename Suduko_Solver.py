import numpy as np

# puzzle[row][col]
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def isValid(row: int, col: int, num: int):
    # check row
    for i in range(9):
        if puzzle[i][col] == num:
            return False

    # check column
    for i in range(9):
        if puzzle[row][i] == num:
            return False

    # check 3x3 matrix
    [sRow, sCol] = 3 * (row//3), 3 * (col//3)
    for x in range(sRow, sRow + 3):
        for y in range(sCol, sCol + 3):
            if puzzle[x][y] == num:
                return False

    return True


def solve():
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    if isValid(row, col, num):
                        puzzle[row][col] = num
                        solve()
                        puzzle[row][col] = 0
                return
    print(np.matrix(puzzle))
    input("More?")


solve()
