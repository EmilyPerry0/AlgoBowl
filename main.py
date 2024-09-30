'''
INPUT
'''
# The first line of the input file is two ints separated by a space, indicating # of rows and cols in the grid
with open('input/ex.txt', 'r') as file:
    rows, cols = map(int, file.readline().split())

    # The next r lines each contain a row of the puzzle. Each line should contain exactly c characters
    grid = [list(line.strip()) for line in file]

num_violations = 0

'''
ALGORITHM
this is a simple algorithm that just puts a lightbulb everywhere we can
'''
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '.':
            grid[row][col] = 'L'

# To print the 2D grid
for row in grid:
    print(row)

'''
VERIFICATION

this section will count the number of violations in the output.
it will also make sure objects that cannot be overwritten are not overwritten 
    (eg a lightbulb cannot be placed on an 'X' or a '2')
'''
for row in range(rows):
    for col in range(cols):
        curr_element = grid[row][col]
        num_lightbulbs = 0

        # check to see if it's a number
        if curr_element == '0' or curr_element == '1' or curr_element == '2' or curr_element == '3' or curr_element == '4':
            # if it is a number convert it to an int so we can compare it to the number of surrounding lightbulbs
            curr_element = int(curr_element)

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
            if not curr_element == num_lightbulbs:
                num_violations = num_violations + 1
            
            num_lightbulbs = 0


'''
OUTPUT
'''

# The first line of output should contain a single integer which is the number of violations as described earlier

with open('output/ex_output.txt', 'w') as file:
    file.write(str(num_violations))

# The next lines each contain exactly c chars. 
# The same chars are used from the input file, with the 'L' replacing '.' chars where lights were added
