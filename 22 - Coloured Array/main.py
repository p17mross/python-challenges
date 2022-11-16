import random

# ANSI escape codes for colours
COLOURS = [
    "\033[1;40m",
    "\033[1;41m",
    "\033[1;42m",
    "\033[1;43m",
    "\033[1;44m",
    "\033[1;45m",
    "\033[1;46m",
    "\033[1;47m",
    "\033[1;100m",
    "\033[1;101m",
    "\033[1;102m",
    "\033[1;103m",
    "\033[1;104m",
    "\033[1;105m",
    "\033[1;106m",
    "\033[1;107m"
]

# ANSI escape code for resetting text colour
RESET = "\033[0m"

# Generate random ints
ints = [
    [
        random.randint(0, 15) for x in range(10)
    ]
    for x in range(10)
]

# Print array
print(ints)

# Print array as coloured rectangle
print("".join([
    "".join([
        COLOURS[cell] + " " 
        for cell in row
    ]) + RESET + "\n" 
    for row in ints
]))