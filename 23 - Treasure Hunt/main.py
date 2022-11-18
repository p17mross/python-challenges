import random

# Create 10x10 list of ints initialised to 0
# 0 = user has not guessed
# 1 = user has guessed
cells = [[0 for _ in range(10)] for _ in range(10)]

# Generate x and y of treasure
x = random.randint(0, 9)
y = random.randint(0, 9)

while True:
    # Get input as int in range 0 <= x <= 9
    try:
        guess_x = int(input("Guess the x coordinate from 0 to 9: "))
        if not (0 <= guess_x <= 9):
            print("Enter an int between 0 and 9")
            continue
        guess_y = int(input("Guess the y coordinate from 0 to 9: "))
        if not (0 <= guess_y <= 9):
            print("Enter an int between 0 and 9")
            continue
    except:
        print("Enter an int")
        continue
    
    # Don't let the user guess the same cell twice
    if cells[guess_x][guess_y] == 1:
        print("You have guessed that cell already!")
        continue

    # Record that the user has guessed the cell
    cells[guess_x][guess_y] = 1

    # Check if the guess is correct
    if guess_x == x and guess_y == y:
        print("You win!")
        break

    # Get the Chebyshev distance (difference in x + difference in y)
    distance = abs(guess_x - x) + abs(guess_y - y)

    # Print message based on distance
    if distance <= 2:
        print("Hot!")
    elif distance <= 4:
        print("Warm")
    else:
        print("Cold.")