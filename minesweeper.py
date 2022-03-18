num_in = int(input())

def count_bombs(board, cell):
    count = 0
    x, y = cell
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if 0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] == '*':
                count += 1
    return count
                
grid_data = []
bomb_locs = []
for i in range(num_in):
    grid_data.append([int(num) for num in input().split(' ')])
    bomb_loc = []
    for j in range(grid_data[i][2]):
        bomb_loc.append([int(num) for num in input().split(' ')])
    bomb_locs.append(bomb_loc)

for i, grid in enumerate(grid_data):
    n_row = grid[0]
    n_col = grid[1]
    n_bom = grid[2]
    
    board = [[-1 for i in range(n_col)] for j in range(n_row)]
    
    bomb_loc = bomb_locs[i]
    for loc in bomb_loc:
        board[loc[0]][loc[1]] = '*'
    
    for y, arr in enumerate(board):
        for x, val in enumerate(arr):
            if val != '*':
                board[y][x] = count_bombs(board, (x, y))
    
    for y, arr in enumerate(board):
        for x, val in enumerate(arr):
            print(val, end='')
        print()