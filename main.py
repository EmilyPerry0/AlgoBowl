import glob

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
ALGORITHM FUNCTION
this is a simple algorithm that just puts a lightbulb everywhere we can
'''
def solver_algo(grid, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '.':
                grid[row][col] = 'L'
    return grid

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
    solved_grid = solver_algo(grid, rows, cols)
    num_violations = count_violations(grid, rows, cols)
    write_output(num_violations, solved_grid, file)
print('solved all boards!')

    