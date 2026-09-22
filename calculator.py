def divide(a, b):
    if b == 0:
        return "division by zero not allowed"
    return a / b


def add(a, b):
    return a + b


if __name__ == "__main__":
    print(divide(10, 0))
    print(add(2, 3))
