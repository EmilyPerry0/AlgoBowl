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
INPUT
'''
# The first line of the input file is two ints separated by a space, indicating # of rows and cols in the grid
with open('output/ex_output.txt', 'r') as file:
    num_violations = map(int, file.readline().split())

    # The next r lines each contain a row of the puzzle. Each line should contain exactly c characters
    grid = [list(line.strip()) for line in file]

counted_violations = 0