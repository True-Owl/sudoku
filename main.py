import sys

def solve_sudoku(sudoku):
    def is_valid(num, row, col):

        for i in range(9):
            if sudoku[row][i] == num or sudoku[i][col] == num:
                return False


        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if sudoku[i][j] == num:
                    return False

        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            sudoku[row][col] = num
                            if backtrack():
                                return True
                            sudoku[row][col] = 0
                    return False
        return True

    if backtrack():
        for row in sudoku:
            print(*row)
    else:
        print("No solution")

if __name__ == '__main__':
    sudoku = []
    for _ in range(9):
        row_input = input().rstrip()
        row = list(map(int, list(row_input)))
        sudoku.append(row)

    print("\n=== 정답 ===\n")
    solve_sudoku(sudoku)
