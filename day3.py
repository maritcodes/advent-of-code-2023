from icecream import ic
import re

bestand = open("complete days/text3.txt", "r")
alltext = bestand.readlines()
alltext = [s.replace('\n', '') for s in alltext]
bestand.close()


def is_symbol(c): # check if character is a symbol (not a digit or a dot)
    return not c.isdigit() and c != '.'


numbers = [] # list of tuples (value, row_index, start_col, end_col)

for row_idx, row in enumerate(alltext): # goes through each row
    for match in re.finditer(r'\d+', row): #\d+ means one or more digits
        start_col = match.start()
        end_col = match.end() - 1 # index of digits
        value = int(match.group()) # value
        numbers.append((value, row_idx, start_col, end_col))

def has_adjacent_symbol(grid, row, start_col, end_col):
    rows = len(grid) # make sure to stay inside the grid bounds
    cols = len(grid[0])
    
    for r in range(row - 1, row + 2):   # check one row above to one row below
        if 0 <= r < rows:  # stay inside grid bounds
            for c in range(start_col - 1, end_col + 2):  # one column left to one column right
                if 0 <= c < cols:  # stay inside grid bounds
                    if is_symbol(grid[r][c]):
                        return True
    return False

def find_gears(alltext): # find all * in alltext
    gears = []
    for row_idx, row in enumerate(alltext):
        for col_idx, char in enumerate(row):
            if char == '*':
                gears.append((row_idx, col_idx))
    return gears
        
def is_adjacent(number, gear_row, gear_col): # is the number adjacent to the gear?
    value, row, start_col, end_col = number
    return (
        row - 1 <= gear_row <= row + 1 and
        start_col - 1 <= gear_col <= end_col + 1
    )

def compute_gear_ratios(grid): # find if gear has two adjacent numbers and compute the gear ratio
    gears = find_gears(grid)

    total = 0

    for gear_row, gear_col in gears:
        adjacent_numbers = [
            num for num in numbers if is_adjacent(num, gear_row, gear_col)
        ]
        # Check if there are exactly two adjacent numbers
        if len(adjacent_numbers) == 2:
            gear_ratio = adjacent_numbers[0][0] * adjacent_numbers[1][0]
            total += gear_ratio

    return total

total = 0
total = compute_gear_ratios(alltext)     
ic(total)

# Part 1 answer: 551094
# Part 2 answer: 80179647