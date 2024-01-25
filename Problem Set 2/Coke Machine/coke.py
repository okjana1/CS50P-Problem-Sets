print("Amount due: 50")
a = 50

while a > 0:
        coin = int(input("Insert coin: "))
        if coin in [5, 10, 25]:
                a -= coin # -= es lo mismo que decir a - coin de manera resumida
                if a > 0:
                        print(f"Amount Due: {a}")
                elif a == "50":
                        print("Change Owed: 0 ")
                else:
                        change = abs(a)
                        print(f"Change Owed: {change}")
        else:
                print("Amount Due: 50")


