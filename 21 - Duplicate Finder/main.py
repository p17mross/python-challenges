# Initialise the sets 'duplicates' and 'names'
duplicates = set()
names = set()

while True:
    # Input name
    name = input("Enter a name, or 'exit' to cancel: ")
    
    if name == "" or name == "exit":
        break
    # Name is a duplcate if it is already in 'names'
    if name in names:
        duplicates.add(name)
    names.add(name)

# Print duplicates
for name in duplicates:
    print(name + " is a duplicate")
