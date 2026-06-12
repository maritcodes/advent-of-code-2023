from icecream import ic

bestand = open("complete days/text4.txt", "r")
alltext = bestand.readlines()
alltext = [s.replace('\n', '') for s in alltext]
bestand.close()

numbers = []
winners = []
matches = []

for line in alltext:
    parts = line.split(': ') # removes card number
    cards = parts[1].split('| ')
    first_part = cards[0].strip().split() # gets all numbers from row
    second_part = cards[1].strip().split()
    winner = list(map(int, first_part)) # make it ints
    number = list(map(int, second_part))
    ws = set(winner) # set of winner
    ns = set(number) # set of number
    matches.append(len(ws & ns))
    winners.append(winner) # stores in list
    numbers.append(number)

def calculate_score(winner, number):
    score = 0
    for num in winner:
        if num in number: # if number is in winner
            score += 1
    if score > 0: # if scored than double the score 
        return 2 ** (score - 1)
    else: 
        return 0
    
def part_2():
    n = len(alltext)

    # Initialize counts: one copy of each starting card
    counts = [1] * n

    # Process each card in order
    for i, m in enumerate(matches):
        if m > 0:
            current_copies = counts[i]
            # Distribute matches to subsequent cards
            for j in range(i + 1, min(n, i + 1 + m)):
                counts[j] += current_copies

    return sum(counts)
    
#total_score = 0
#for winner, number in zip(winners, numbers):
#    score = calculate_score(winner, number) # one score
#    total_score += score    
#ic(total_score)
counts = part_2()
ic(counts)

# Part 1 answer: 21485
# Part 2 answer: 11024379