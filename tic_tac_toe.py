from audioop import minmax
import copy

class Board:
    def __init__(self, board) -> None:
        self.board = board
        self.turn = True
    
    def play_move(self, move, char):
        x, y = move
        self.board[y][x] = char
        self.turn = not self.turn
        return self
    
    def did_win(self):
        for arr in self.board:
            if all([v == 'X' for v in arr]):
                return 1
            elif all([v == 'O' for v in arr]):
                return 2
        for i, val in enumerate(self.board):
            if all([v[i] == 'X' for v in self.board]):
                return 1
            elif all([v[i] == 'O' for v in self.board]):
                return 2
        
        if all([arr[i] == 'X' for i, arr in enumerate(self.board)]):
            return 1
        elif all([arr[i] == 'O' for i, arr in enumerate(self.board)]):
            return 2
        
        if all([arr[len(arr) - i - 1] == 'X' for i, arr in enumerate(self.board)]):
            return 1
        elif all([arr[len(arr) - i - 1] == 'O' for i, arr in enumerate(self.board)]):
            return 2
        elif all([all([val == 'X' or val == 'O' for val in arr]) for arr in self.board]):
            return 3
        
        return 0
    
    def get_board(self):
        return self.board
    
    def get_turn(self):
        return self.turn

class TicTacToe:
    def __init__(self, board) -> None:
        self.board = Board(board)
    
    def minimax(self, board, depth):
        if board.did_win() == 1:
            return 1# - depth
        if board.did_win() == 2:
            return -1# + depth
        if board.did_win() == 3:
            return 0
        
        
        if board.get_turn():
            max_score = -999999
            for y, row in enumerate(board.get_board()):
                for x, val in enumerate(row):
                    if val == '*':
                        score = self.minimax(copy.deepcopy(board).play_move((x, y), 'X'), depth + 1)
                        if max_score < score:
                            max_score = score
            return max_score  
        else:
            min_score = 999999
            for y, row in enumerate(board.get_board()):
                for x, val in enumerate(row):
                    if val == '*':
                        score = self.minimax(copy.deepcopy(board).play_move((x, y), 'O'), depth + 1)
                        if min_score > score:
                            min_score = score
            return min_score
    
    def get_best_move(self):
        coords = (0, 0)
        best_score = -999999
        for y, row in enumerate(self.board.get_board()):
            for x, val in enumerate(row):
                if val == '*' and self.board.get_turn():
                    score = self.minimax(copy.deepcopy(self.board).play_move((x, y), 'X'), 0)
                    if score > best_score:
                        best_score = score
                        coords = (x, y)
        
        return self.board.play_move(coords, 'X').get_board()

num_games = int(input())
games_arr = []
for i in range(num_games):
    game_arr = []
    for irow in range(3):
        arr = list(input())
        game_arr.append(arr)
    games_arr.append(game_arr)

for game in games_arr:
    game_obj = TicTacToe(game)
    best_move = game_obj.get_best_move()
    for arr in best_move:
        for val in arr:
            print(val, end='')
        print()