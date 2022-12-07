# The grade letters / numbers
GRADES = "U123456789"
# The grade boundaries
BOUNDARIES = [2, 4, 13, 22, 31, 41, 54, 57, 80]

# Gets the grade for a given mark
def GetGrade(mark):
    for (i, boundary) in enumerate(BOUNDARIES):
        if mark < boundary:
            return GRADES[i]
    # If higher than the top grade boundary
    return GRADES[len(GRADES) - 1]

# Gets how many marks to the next grade
def MarksToNextGrade(mark):
    for (i, boundary) in enumerate(BOUNDARIES):
        if mark < boundary:
            return BOUNDARIES[i] - mark
    # If higher than the top grade boundary
    return None

mark = int(input("Enter your mark: "))
print("Your grade is {}.".format(GetGrade(mark)))
to_next = MarksToNextGrade(mark)
if to_next != None:
    print("You need", to_next, "marks to get the next grade.")
else:
    print("You got the top grade!")