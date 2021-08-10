board = [[0,0,8,0,0,0,2,0,0],
        [0,0,0,0,8,4,0,9,0],
        [0,0,6,3,2,0,0,1,0],
        [0,9,7,0,0,0,0,8,0],
        [8,0,0,9,0,3,0,0,3],
        [0,1,0,0,0,0,0,9,5],
        [0,7,0,0,4,5,8,0,0],
        [0,3,0,7,1,0,0,0,0],
        [0,0,8,0,0,0,0,4,0]]

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

def get_square(i,j,bo):
        start_col, end_col = get_square_range(i,bo)
        start_row, end_row = get_square_range(j,bo)

        rows_from_board = bo[start_row:end_row+1]
        square = [row[start_col:end_col+1] for row in rows_from_board]
        return(square)


def get_square_range(x,bo):
        start_index = int(x/3) * 3
        end_index = start_index + 2
        print(start_index,end_index)
        return (start_index, end_index)

print_board(board)
print(valid_entry(8,4,0,board))
