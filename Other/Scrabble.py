# The values of letters
SCRABBLE_SCORES = [
    "",                  # 0 points
    "EAIONRTLSU",        # 1 points
    "DG",                # 2 points
    "BCMP",              # 3 points
    "FHVWY",             # 4 points
    "K",                 # 5 points
    "","",               # Skip 6 and 7
    "JX",                # 8 points
    "",                  # Skip 9
    "QZ"                 # 10 points
]

# Gets the value of a letter
def ScrabbleLetterValue(letter):
    for (i, set) in enumerate(SCRABBLE_SCORES):
        if letter.upper() in set: return i
    raise ValueError(f"Letter not found: {letter}")

# Gets the total value of a word
def ScrabbleWordValue(word):
    total = 0
    for letter in word:
        total += ScrabbleLetterValue(letter)
    return total

word = input("Enter a word: ")
print(f"The scrabble value of '{word}' is {ScrabbleWordValue(word)}")