fruit = input("Item: ").capitalize().title()
d = {
    "Apple": "130",
    "Avocado": "50",
    "Sweet Cherries": "100",
    "Kiwifruit": "90",
    "Pear": "100"
}

if fruit in d:
    print(f"Calories: ", (d[fruit]))
else:
    print("")
