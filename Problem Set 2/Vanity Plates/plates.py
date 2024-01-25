def main():
    plate: str = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s: str) -> bool:
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    foundNum: bool = False
    firstNum: bool = True
    for c in s:
        if c.isdigit():
            foundNum = True
            if firstNum:
                if c == "0":
                    return False
                firstNum = False
        elif c.isalpha():
            if foundNum:
                return False
        else:
            return False
    return True

main()
