from icecream import ic
import math

bestand = open("complete days/text2.txt", "r")
alltext = bestand.readlines()
alltext = [s.replace('\n', '') for s in alltext]
bestand.close()

total = 0

def is_game_possible(line):
    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    # Split into "Game X:" and the draws
    game_info, draws = line.split(':')
    
    # Extract game ID
    game_id = int(game_info.split()[1])

    # Split all draws into separate sets
    subsets = draws.strip().split(';')

    for subset in subsets:

        # For each subset, parse the individual cube counts
        cubes = subset.strip().split(',')

        for cube in cubes:
            parts = cube.strip().split()
            count = int(parts[0])
            color = parts[1]
            
            if count > min_cubes[color]:
                min_cubes[color] = count  # if the count is greater than the current minimum, update it

    result = math.prod(min_cubes.values())
    return result  # Game is possible

for line in alltext:
    result = is_game_possible(line)
    total += result

ic(total)

# Part 1 answer: 2377
# Part 2 answer: 71220