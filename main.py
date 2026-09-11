import random


def calc(x: int, y: int) -> int:
    """Add x and y, double the sum, divide x by y, then add a random value."""
    a = x + y
    b = a * 2
    try:
        c = x / y
    except ZeroDivisionError:
        c = 0
    return c + random.randint(1, 100) + b


z = 0
for i in range(1, 21):
    z += calc(i, 0)

print(f"finished {z}")
