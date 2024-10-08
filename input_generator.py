import random
import numpy as np

'''
HELPER FUNCTIONS
'''
def thresh(x, row):
    return x <= -(float(row)/1000.0) + 0.4



'''
GENERATION
'''
rows = 316
cols = 316

grid = np.zeros((rows,cols))
secondary_grid = np.full((rows,cols), ' ')

# generate a random number between 0 and 1 for each cell
for row in range(rows):
    for col in range(cols):
        grid[row][col] = random.random()

# see if a cell should become a numbered block
for row in range(rows):
    for col in range(cols):
        if not thresh(grid[row][col], row):
            secondary_grid[row][col] = '0'
        else:
            secondary_grid[row][col] = '1'

# figure out what number each block should be
for row in range(rows):
    for col in range(cols):
        if secondary_grid[row][col] == '1':
            new_rand_num = random.random()
            if new_rand_num < 0.016:
                to_assign_num = '4'
            elif new_rand_num < 0.064:
                to_assign_num = '3'
            elif new_rand_num < 0.144:
                to_assign_num = '2'
            elif new_rand_num < 0.256:
                to_assign_num = '1'
            elif new_rand_num < 0.4:
                to_assign_num = '0'
            else:
                to_assign_num = 'X'
            secondary_grid[row][col] = to_assign_num
        else:
            secondary_grid[row][col] = '.'
            


'''
OUTPUT
'''
with open('generated_input.txt', 'w') as file:
    # The first line of input should contain two ints: rows cols
    file.write(f'{rows} {cols}' + '\n')

    # The next lines each contain exactly c chars. 
    # The same chars are used from the input file, with the 'L' replacing '.' chars where lights were added
    for row in secondary_grid:
        file.write(''.join(map(str, row)) + '\n')