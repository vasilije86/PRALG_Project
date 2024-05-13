class Board:
    def __init__(self, board):
        self.board = board

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, num, position):
        for i in range(9):
            if self.board[position[0]][i] == num and position[1] != i:
                return False

    
        for i in range(9):
            if self.board[i][position[1]] == num and position[0] != i:
                return False

        box_x = position[1] // 3
        box_y = position[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != position:
                    return False

        return True

    def solve(self):
        find = self.find_empty_cell()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

def solve_sudoku(puzzle):
    sudoku_board = Board(puzzle)
    if sudoku_board.solve():
        return sudoku_board.board
    else:
        return None
