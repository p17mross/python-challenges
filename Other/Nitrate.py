# A function to calculate the dose of carbon for a given nitrate level
def CalculateDose(nitrate_level):
    if nitrate_level > 10:
        return 3
    if nitrate_level > 2.5:
        return 2
    if nitrate_level > 1:
        return 1
    return 0.5

nitrate_level = float(input("Enter the nitrate level: "))
print(f"for {nitrate_level} nitrate, use {CalculateDose(nitrate_level)}ml of carbon")