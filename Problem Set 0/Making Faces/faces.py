def main():
    msg = input ()
    print(convert(msg))

def convert(msg):
    msg = msg.replace(":)", "🙂").replace(":(", "🙁")
    return msg

main ()
