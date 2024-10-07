import numpy as np

rows = 316
cols = 316

grid = np.zeros((rows,cols), dtype=int)

'''
OUTPUT
'''
with open('generated_input.txt', 'w') as file:
    # The first line of input should contain two ints: rows cols
    file.write(f'{rows} {cols}' + '\n')

    # The next lines each contain exactly c chars. 
    # The same chars are used from the input file, with the 'L' replacing '.' chars where lights were added
    for row in grid:
        file.write(''.join(map(str, row)) + '\n')