def main():
    name = input('whats your name?').strip().title()
    hello(name)


def hello(to="world"):
    print("hello,",to)

main()

