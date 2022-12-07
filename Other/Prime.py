# Function to check if a number is prime
def IsPrime(n):
    if n < 2: return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if IsPrime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")