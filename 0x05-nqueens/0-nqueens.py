mport sys

def is_safe(board, row, col, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, N, result):
    # If all queens are placed then return true
    if col == N:
        result.append([[row, col] for row in range(N) if board[row][col] == 1])
        return True
    
    res = False
    for i in range(N):
        # Check if queen can be placed on board[i][col]
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1
            
            # recur to place rest of the queens
            res = solve_n_queens_util(board, col + 1, N, result) or res
            
            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0
    
    return res

def solve_n_queens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    solve_n_queens_util(board, 0, N, result)
    for solution in result:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
