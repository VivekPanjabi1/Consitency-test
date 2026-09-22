import math


def divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b


def safe_sqrt(x):
    if x < 0:
        return math.sqrt(abs(x))
    return math.sqrt(x)


if __name__ == "__main__":
    print(divide(10, 0))
    print(safe_sqrt(-9))
