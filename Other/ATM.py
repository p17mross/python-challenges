# Holds the info about all registered accounts
accounts = {
    #account no: [pin, balance]
    "1111-0000": ["1111", 1_00],
    "1234-5678": ["2345", 100_00]
}

# Prints an error message to the user
def showError(e):
    print("Error: " + e)

# Waits until a card is entered and returns its card number
def waitForCardEntered():
    while True:
        cardNumber = input("Enter your card number: ")
        if cardNumber in accounts:
            return cardNumber
        showError("Invalid card number")

# Gets the pin of a card given its card number
def getCardPIN(cardNumber):
    return accounts[cardNumber][0]

# Prompts the user to enter their PIN and returns it, or None if the user selects cancel
def getUserPIN():
    while True:
        PIN = input("Enter your pin (or 'cancel' to cancel the transaction): ")
        if PIN == "cancel": return None
        # Only let the user enter 4 digits
        if len(PIN) != 4 or any([(PIN[x] not in "0123456789") for x in range(4)]):
            showError("PIN must be 4 digits")
            continue
        return PIN

# Gets the balance of a card given its card number
def getCardBalance(cardNumber):
    return accounts[cardNumber][1]

# Tells the user their balance
def displayBalance(cardNumber):
    print("Your balance is £%.2f" % (accounts[cardNumber][1] / 100.0))

# Prompts the user to enter an amount of money and returns it, or None if the user selects cancel
def getAmount():
    while True:
        amount = input("Enter the amount (of 'cancel' to cancel the transaction): £")
        if amount == "cancel": return None

        try:
            amount = float(amount)
            if amount <= 0:
                showError("Amount must be positive")
                continue
            return int(amount * 100)
        except:
            showError("Invalid entry")

# Outputs the money from the ATM
def dispenseMoney(amount):
    input("Take this £%.2f" % (amount / 100.0))

# Sets the balance of a card given its card number
def setCardBalance(cardNumber, balance):
    accounts[cardNumber][1] = balance

# Wait for the user to remove their card
def waitForCardRemoved():
    input("Remove your card")

# Each iteration of this loop is one withdrawal
while True:

    # Stores whether the user has cancelled the transaction
    cancelled = False

    # Wait for the user to enter their card
    cardNumber = waitForCardEntered()
    # Get the PIN of the card
    cardPIN = getCardPIN(cardNumber)
    # Loop until the user enters the correct PIN
    while True:
        userPIN = getUserPIN()
        if userPIN == None:
            cancelled = True
            break
        if cardPIN == userPIN: break
        showError("Wrong PIN")
    # Move to next transaction if cancelled
    if cancelled: waitForCardRemoved();continue

    balance = getCardBalance(cardNumber)
    displayBalance(cardNumber)

    while True:
        withdrawal = getAmount()
        if withdrawal == None:
            cancelled = True
            break
        if withdrawal <= balance: break
        showError("Not enough balance")

    # Move to next transaction if cancelled
    if cancelled: waitForCardRemoved();continue

    dispenseMoney(withdrawal)
    setCardBalance(cardNumber, balance - withdrawal)

    waitForCardRemoved()

    
