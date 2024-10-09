import glob
import copy
import queue

'''
HELPER FUNCTIONS
'''
def scan_cell_directions(grid, row, col, target_char):
  """Scans the cell at (row, col) in all four directions until hitting an edge, a specified wall character, or finding the target character.

  Args:
    grid: The 2D grid of characters.
    row: The row index of the cell to scan.
    col: The column index of the cell to scan.
    target_char: The character to search for.

  Returns:
    True if the target character is found in any of the adjacent cells until an edge or wall, False otherwise.
  """

  rows = len(grid)
  cols = len(grid[0])
  wall_chars = ['X', '0', '1', '2', '3', '4']

  # Check up
  r = row - 1
  while r >= 0 and grid[r][col] != target_char and all(grid[r][col] != wall_char for wall_char in wall_chars):
    r -= 1
  if r >= 0 and grid[r][col] == target_char:
    return True

  # Check down
  r = row + 1
  while r < rows and grid[r][col] != target_char and all(grid[r][col] != wall_char for wall_char in wall_chars):
    r += 1
  if r < rows and grid[r][col] == target_char:
    return True

  # Check left
  c = col - 1
  while c >= 0 and grid[row][c] != target_char and all(grid[row][c] != wall_char for wall_char in wall_chars):
    c -= 1
  if c >= 0 and grid[row][c] == target_char:
    return True

  # Check right
  c = col + 1
  while c < cols and grid[row][c] != target_char and all(grid[row][c] != wall_char for wall_char in wall_chars):
    c += 1
  if c < cols and grid[row][c] == target_char:
    return True

  return False

def light_up_squares(grid, row, col):
    wall_chars = ['X', '0', '1', '2', '3', '4']
    rows = len(grid)
    cols = len(grid[0])   

    # traverse in the up dir
    r = row - 1
    while r >= 0 and all(grid[r][col] != wall_char for wall_char in wall_chars):
        grid[r][col] = '+'
        r -= 1
    
    # traverse in the down dir
    r = row + 1
    while r < rows and all(grid[r][col] != wall_char for wall_char in wall_chars):
        grid[r][col] = '+'
        r += 1

    # traverse in the left dir
    c = col - 1
    while c >= 0 and all(grid[row][c] != wall_char for wall_char in wall_chars):
        grid[row][c] = '+'
        c -= 1

    # traverse in the left dir
    c = col + 1
    while c < cols and all(grid[row][c] != wall_char for wall_char in wall_chars):
        grid[row][c] = '+'
        c += 1
    
    return grid

def get_num_adj_avail_cells(grid, row, col):
    num_avail_cells = 0
    rows = len(grid)
    cols = len(grid[0])  

    if row != 0 and grid[row - 1][col] == '.':
        num_avail_cells += 1
    if row != rows - 1 and grid[row + 1][col] == '.':
        num_avail_cells += 1
    if col != 0 and grid[row][col -1] == '.':
        num_avail_cells += 1
    if col != cols - 1 and grid[row][col + 1] == '.':
        num_avail_cells += 1
    return num_avail_cells

def fancy_light_up(grid, row, col, q):
    wall_chars = ['X', '0', '1', '2', '3', '4']
    rows = len(grid)
    cols = len(grid[0])   

    # traverse in the up dir, adding num tiles to q
    r = row - 1
    while r >= 0 and all(grid[r][col] != wall_char for wall_char in wall_chars):
        grid[r][col] = '+'

        if r != 0:
            adj_up = grid[r - 1][col]
        if r != rows - 1:
            adj_down = grid[r + 1][col]
        if col != 0:
            adj_left = grid[r][col - 1]
        if col != cols - 1:
            adj_right = grid[r][col + 1]

        if r != 0 and (adj_up == '1' or adj_up == '2' or adj_up == '3'):
            q.put((r-1,col))
        if r != rows - 1 and (adj_down == '1' or adj_down == '2' or adj_down == '3'):
            q.put((r+1,col))
        if col != 0 and (adj_left == '1' or adj_left == '2' or adj_left == '3'):
            q.put((r,col-1))
        if col != cols - 1 and (adj_right == '1' or adj_right == '2' or adj_right == '3'):
            q.put((r,col+1))

        r -= 1
    
    # traverse in the down dir, adding num tiles to q
    r = row + 1
    while r < rows and all(grid[r][col] != wall_char for wall_char in wall_chars):
        grid[r][col] = '+'

        if r != 0:
            adj_up = grid[r - 1][col]
        if r != rows - 1:
            adj_down = grid[r + 1][col]
        if col != 0:
            adj_left = grid[r][col - 1]
        if col != cols - 1:
            adj_right = grid[r][col + 1]

        if r != 0 and (adj_up == '1' or adj_up == '2' or adj_up == '3'):
            q.put((r-1,col))
        if r != rows - 1 and (adj_down == '1' or adj_down == '2' or adj_down == '3'):
            q.put((r+1,col))
        if col != 0 and (adj_left == '1' or adj_left == '2' or adj_left == '3'):
            q.put((r,col-1))
        if col != cols - 1 and (adj_right == '1' or adj_right == '2' or adj_right == '3'):
            q.put((r,col+1))

        r += 1

    # traverse in the left dir, adding num tiles to q
    c = col - 1
    while c >= 0 and all(grid[row][c] != wall_char for wall_char in wall_chars):
        grid[row][c] = '+'

        if row != 0:
            adj_up = grid[row - 1][c]
        if row != rows - 1:
            adj_down = grid[row + 1][c]
        if c != 0:
            adj_left = grid[row][c - 1]
        if c != cols - 1:
            adj_right = grid[row][c + 1]

        if row != 0 and (adj_up == '1' or adj_up == '2' or adj_up == '3'):
            q.put((row-1,c))
        if row != rows - 1 and (adj_down == '1' or adj_down == '2' or adj_down == '3'):
            q.put((row+1,c))
        if c != 0 and (adj_left == '1' or adj_left == '2' or adj_left == '3'):
            q.put((row,c-1))
        if c != cols - 1 and (adj_right == '1' or adj_right == '2' or adj_right == '3'):
            q.put((row,c+1))
        
        c -= 1

    # traverse in the left dir, adding num tiles to q
    c = col + 1
    while c < cols and all(grid[row][c] != wall_char for wall_char in wall_chars):
        grid[row][c] = '+'

        if row != 0:
            adj_up = grid[row - 1][c]
        if row != rows - 1:
            adj_down = grid[row + 1][c]
        if c != 0:
            adj_left = grid[row][c - 1]
        if c != cols - 1:
            adj_right = grid[row][c + 1]

        if row != 0 and (adj_up == '1' or adj_up == '2' or adj_up == '3'):
            q.put((row-1,c))
        if row != rows - 1 and (adj_down == '1' or adj_down == '2' or adj_down == '3'):
            q.put((row+1,c))
        if c != 0 and (adj_left == '1' or adj_left == '2' or adj_left == '3'):
            q.put((row,c-1))
        if c != cols - 1 and (adj_right == '1' or adj_right == '2' or adj_right == '3'):
            q.put((row,c+1))

        c += 1
    
    return grid,q


'''
INPUT FUNCTIONS
'''
def get_all_files():
    return glob.glob("input/input_group*.txt")  # Replace "*.txt" with your file extension
   
def get_input_info(filename):
    with open(filename, 'r') as file:
        # row and col info, and grid generation
        rows, cols = map(int, file.readline().split())
        return  rows, cols, [list(line.strip()) for line in file]

'''
ALGORITHM FUNCTIONS
this is a simple algorithm that just puts a lightbulb everywhere we can
'''
def solver_algo(grid, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '.':
                grid[row][col] = 'L'
    return grid

'''
REAL ALGOS
'''
def all_xs_algo(grid, rows, cols):
    lit_up_grid = copy.deepcopy(grid)
    for row in range(rows):
        for col in range(cols):
            if(lit_up_grid[row][col] == '.'):
                # if the cell isn't lit up yet, place a lightbulb 
                grid[row][col] = 'L'
                # then light up the squares it lights up in the lit_up_grid
                lit_up_grid = light_up_squares(lit_up_grid, row, col)
    return grid

def charlies_improvement_algo(grid, rows, cols):
    # refrence grid char keys:
    #   X,0,1,2,3,4,.,L == defined in problem
    #   + == lit up
    #   - == temporarily avoid (from zeros n such) 
    refrence_grid = copy.deepcopy(grid)
    q = queue.Queue()

    # mark all spaces around zeros as not placeable
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '0':
                if row != 0 and grid[row - 1][col] == '.':
                    refrence_grid[row - 1][col] = '-'
                if row != rows - 1 and grid[row + 1][col] == '.':
                    refrence_grid[row + 1][col] = '-'
                if col != 0 and grid[row][col -1] == '.':
                    refrence_grid[row][col - 1] = '-'
                if col != cols - 1 and grid[row][col + 1] == '.':
                    refrence_grid[row][col - 1] = '-'
                
    # find all pieces that have matching number of available tiles around it to num requried
    #   then place lights there
    # when lighting each tile, check all tiles that touch the lighting path to see if they are number tiles
    #   if they are, add them to a queue or stack, then evaluate those tiles next
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            if cell == '1' or cell == '2' or cell == '3' or cell == '4':
                cell_num = int(cell)
                if cell_num == get_num_adj_avail_cells(refrence_grid, row, col):
                    refrence_grid, q = fancy_light_up(refrence_grid, row, col, q)
                    if not q.empty():
                        
                



    

'''
VERIFICATION FUNCTION

this section will count the number of violations in the output.
it will also make sure each blank cell is lit up.
it will also make sure objects that cannot be overwritten are not overwritten 
    (eg a lightbulb cannot be placed on an 'X' or a '2') TODO!
'''
# count violations
def count_violations(grid, rows, cols):
    num_violations = 0
    for row in range(rows):
        for col in range(cols):
            curr_element = grid[row][col]
            num_lightbulbs = 0

            # check to see if it's a number
            if curr_element == '0' or curr_element == '1' or curr_element == '2' or curr_element == '3' or curr_element == '4':

                # loop over the four surrounding squares and count the number of lightbulbs
                if row != 0 and grid[row - 1][col] == 'L':
                    num_lightbulbs = num_lightbulbs + 1
                if row != rows - 1 and grid[row + 1][col] == 'L':
                    num_lightbulbs = num_lightbulbs + 1
                if col != 0 and grid[row][col - 1] == 'L':
                    num_lightbulbs = num_lightbulbs + 1
                if col != cols - 1 and grid[row][col + 1] == 'L':
                    num_lightbulbs = num_lightbulbs + 1
                
                # its a violation if the number of lightbults does not match curr_element number
                if not int(curr_element) == num_lightbulbs:
                    num_violations = num_violations + 1
                
                num_lightbulbs = 0
            
            # check to see if it's a lightbulb
            elif curr_element == 'L':
                # scan in all directions to see if the lightbulb lights up another lightbulb
                if scan_cell_directions(grid, row, col, 'L'):
                    num_violations += 1

    # make sure each cell is lit up
    for row in range(rows):
        for col in range(cols):
            # the only cells we care about are the '.' ones
            if grid[row][col] == '.':
                # scan in all directions to see if there's a lightbulb.
                # if we don't find a lightbulb in any direction even once, the solution is invalid.
                if not scan_cell_directions(grid, row, col, target_char='L'):
                    raise ValueError("Solution Invalid! Not all cells lit up.")
    return num_violations



'''
OUTPUT FUNCTION
'''
def write_output(num_violations, grid, filename):
    with open(f'output/output_{filename[12:]}', 'w') as file:
        # The first line of output should contain a single integer (number of violations)
        file.write(str(num_violations) + '\n')

        # The next lines each contain exactly c chars. 
        # The same chars are used from the input file, with the 'L' replacing '.' chars where lights were added
        for row in grid:
            file.write(''.join(map(str, row)) + '\n')

'''
PROGRAM FLOW CODE
'''
files = get_all_files()
for file in files:
    rows, cols, grid = get_input_info(file)
    solved_grid = all_xs_algo(grid, rows, cols)
    num_violations = count_violations(grid, rows, cols)
    write_output(num_violations, solved_grid, file)
    print(f'solved board: {file}')
print('solved all boards!')

    