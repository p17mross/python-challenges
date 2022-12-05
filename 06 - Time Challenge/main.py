import time

input("Press enter as close to 10s apart as possible: ")
# Record start time
start_time = time.time()

# Wait for the user to press enter again
input()
# Record end time
end_time = time.time()

# Calculate time elapsed
difference = end_time - start_time

# Print time elapsed
print("That was " + str(difference) + " seconds. ")
# Print how far from 10s
print("That's " + str(abs(10 - difference)) + " seconds too " + ("little" if difference < 10 else "much"))