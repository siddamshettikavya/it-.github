
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise SystemExit("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    first, second = 10, 5
    print(f"{first} + {second} = {add(first, second)}")
    print(f"{first} - {second} = {subtract(first, second)}")
    print(f"{first} * {second} = {multiply(first, second)}")
    print(f"{first} / {second} = {divide(first, second)}")
