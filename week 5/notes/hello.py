def main():
    name = input("What's yout name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()