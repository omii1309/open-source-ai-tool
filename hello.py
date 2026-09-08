def greet_user(name):
    return f"Hello, {name}! Welcome to the Open Source AI Tool."


def main():
    name = input("What is your name? ")
    message = greet_user(name)
    print(message)


if __name__ == "__main__":
    main()
