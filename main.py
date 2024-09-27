'''
INPUT
'''
# The first line of the input file is two ints separated by a space, indicating # of rows and cols in the grid
with open('input/ex.txt', 'r') as file:
    rows, cols = map(int, file.readline().split())
    grid = [list(line.strip()) for line in file]

# The next r lines each contain a row of the puzzle. Each line should contain exactly c characters
num_violations = 0

'''
ALGORITHM
'''

'''
VERIFICATION

this section will count the number of violations in the output.
it will also make sure objects that cannot be overwritten are not overwritten 
    (eg a lightbulb cannot be placed on an 'X' or a '2')
'''

'''
OUTPUT
'''

# The first line of output should contain a single integer which is the number of violations as described earlier

with open('output/ex_output.txt', 'w') as file:
    file.write(str(num_violations))

# The next lines each contain exactly c chars. 
# The same chars are used from the input file, with the 'L' replacing '.' chars where lights were added
