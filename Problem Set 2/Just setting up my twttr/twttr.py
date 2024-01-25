text = str(input("Input "))
for c in text:
    if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print("", end="")
    else:
        print(c, end="")


