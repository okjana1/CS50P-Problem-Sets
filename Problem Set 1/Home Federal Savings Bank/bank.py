#greet = str(input("Greeting: ")).lower().strip().split()

user = input("Greeting: ").lower().strip()

if user.startswith("hello"):
    print ("$0")

elif user.startswith("h") and not user.startswith("hello"):
    print("$20")
else:
    print("$100")
