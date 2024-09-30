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
            curr_row = row
            curr_col = col
            violation_found = False

            # scan up
            while curr_row != 0:
                curr_row = curr_row - 1
                if grid[curr_row][col] == 'L':
                    num_violations = num_violations + 1
                    violation_found = True
                    break
                # walls and numbers block light
                elif grid[curr_row][col] != '.':
                    break

            # scan down
            if not violation_found:
                curr_row = row
                while curr_row != rows - 1:
                    curr_row = curr_row + 1
                    if grid[curr_row][col] == 'L':
                        num_violations = num_violations + 1
                        violation_found = True
                        break
                    # walls and numbers block light
                    elif grid[curr_row][col] != '.':
                        break

            # scan left
            if not violation_found:
                while curr_col != 0:
                    curr_col = curr_col - 1
                    if grid[row][curr_col] == 'L':
                        num_violations = num_violations + 1
                        violation_found = True
                        break
                    # walls and numbers block light
                    elif grid[row][curr_col] != '.':
                        break

            # scan right
            if not violation_found:
                curr_col = col
                while curr_col != cols - 1:
                    curr_col = curr_col + 1
                    if grid[row][curr_col] == 'L':
                        num_violations = num_violations + 1
                        violation_found = True
                        break
                    # walls and numbers block light
                    elif grid[row][curr_col] != '.':
                        break




'''
OUTPUT
'''
with open('output/ex_output.txt', 'w') as file:
    # The first line of output should contain a single integer (number of violations)
    file.write(str(num_violations) + '\n')

    # The next lines each contain exactly c chars. 
    # The same chars are used from the input file, with the 'L' replacing '.' chars where lights were added
    for row in grid:
        file.write(''.join(map(str, row)) + '\n')