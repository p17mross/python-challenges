# Takes a string containing '1' and '0'
# Returns True if the number of '1's is odd, False if it is even 
def OddParity(sequence):
    num_ones = 0
    for bit in sequence:
        if bit == "1":
            num_ones += 1
    return num_ones % 2 == 1

# Does the same as OddParity but fancier
def OddParityComprehension(sequence):
    return sum([bit == "1" for bit in sequence]) % 2 == 1

sequence = input("Enter a bit sequence: ")
if OddParity(sequence):
    print("The string passes")
else:
    print("The string fails")