import random
print("Vending Machine")
print("1. Cola (5k)")
print("2. Matcha (15k)")
print("3. Pepsi (10k)")
print("4. Surprise me!")
choice = input("Your choice: ")

drinks = {
    "1" : "Cola",
    "2" : "Matcha",
    "3" : "Pepsi",
    "4" : random.choice(["Cola", "Matcha", "Pepsi", "\"The Mysterious Drink!\""])
}

print("Here is your " + drinks.get(choice, "-Invalid-"))

