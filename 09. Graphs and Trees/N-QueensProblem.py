def dfs_n_queens(n) -> list:
    if n < 1:
        return []

    solutions = []

    def is_safe(queens, row, col):
        for r, c in enumerate(queens):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def place_queens(row, queens):
        if row == n:
            solutions.append(queens.copy())
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)
                place_queens(row + 1, queens)
                queens.pop()

    place_queens(0, [])
    return solutions


print(dfs_n_queens(4))