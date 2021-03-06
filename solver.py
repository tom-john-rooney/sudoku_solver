board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# pretty prints a board on the console
def print_board(bo):
        print('='*37)
        for i, row in enumerate(bo):
                row_vals = [x if x != 0 else ' ' for x in row]
                print(('|' + ' {} | {} | {} |'*3).format(*row_vals)) # unpacks row values into string for row
                if i == 8:
                        print('='*37)
                elif i % 3 == 2:
                        print('|' + '===|'*8 + '===|')
                else:
                        print('|' + '   |'*8 + '   |')

# finds the first empty space on the board
def find_first_empty(bo):
        for i in range(len(bo)):
                for j in range(len(bo)):
                        if bo[i][j] == 0:
                                return (i,j)
        return None

# checks if digit e at board coordinates i,j is valid given the rules of the game
def valid_entry(e,i,j,bo):
        row = bo[i]
        col = [row[j] for row in bo]
        square = get_square(i,j,bo)

        valid_row = not(e in row)
        valid_col = not(e in col)
        valid_square = not(any(e in row for row in square))

        if(valid_row & valid_col & valid_square):
                return True
        else:
                return False

# extrapolates the 3x3 subgrid containing the given coordinate on the board
def get_square(i,j,bo):
        start_col, end_col = get_square_range(j,bo)
        start_row, end_row = get_square_range(i,bo)

        rows_from_board = bo[start_row:end_row+1]
        square = [row[start_col:end_col+1] for row in rows_from_board]
        return(square)

# helper function for get_square, finds the index range for the rows and columns of the square in question
def get_square_range(x,bo):
        start_index = int(x/3) * 3
        end_index = start_index + 2
        return (start_index, end_index)

# implementation of backtracking algorithm using previously defined helper functions
def solve_board(bo):
        empty = find_first_empty(bo)
        if(not empty):
                return True
        else:
                row, col = empty

        for i in range(1,10):
                if(valid_entry(i, row, col, bo)):
                        bo[row][col] = i

                        if(solve_board(bo)):
                                return True
                        else:        
                                bo[row][col] = 0
        
        return False

print("Original puzzle:")
print_board(board)
if(solve_board(board)):
        print("Solution:")
        print_board(board)
else:
        print("No solution to this puzzle!")
