from icecream import ic

bestand = open("complete days/text1.txt", "r")
alltext = bestand.readlines()
alltext = [s.replace('\n', '') for s in alltext]
bestand.close()

total = [] # list to store the first and last number of each line
numbers = [] # list to store all numbers from the text
words = []

def replace_written_numbers(s): # replace written numbers with digits
    word_to_digit = { # Mapping of written numbers to digits
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    words_sorted = sorted(word_to_digit.keys(), key=lambda x: -len(x)) # Sort by length to match longer words first
    result = ''
    i = 0
    while i < len(s):
        matched = False
        for word in words_sorted: # Check for each word in the sorted list
            if s.startswith(word, i): # Check if the word matches at the current position
                result += word_to_digit[word]
                matched = True
                break
        if not matched: # If no word matched, just append the current character
            if s[i].isdigit():
                result += s[i]
        i += 1  # Always advance by 1 to allow overlaps
    return result
'''
def get_numbers(text): # get all numbers from text
    numbers = []
    for line in text:
        n = []
        for char in line:
            if char.isdigit():
                n.append(int(char))
        numbers.append(n)
    return numbers
'''
def get_first_and_last_number(text): # get the first and last number of each line
    for n in numbers:
        first_number = n[0]
        last_number = n[-1]
        total.append(str(first_number) +str(last_number))
    return total

# Main execution
for s in alltext:
    s = replace_written_numbers(s)
    words.append(s) # list of digits
total = get_first_and_last_number(words)
ans = sum(int(t) for t in total) 
ic(ans)  # Print the final answer

# Part 1 answer: 54239
# Part 2 answer: 55343