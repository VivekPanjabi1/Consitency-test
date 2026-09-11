import random

MAX_RANGE = 20
MIN_RANDOM = 1
MAX_RANDOM = 100
MULTIPLIER = 2
DEFAULT_DIVISOR = 0


def calc(x: int, y: int) -> int:
    """Add x and y, double the sum, divide x by y, then add a random value."""
    a = x + y
    b = a * MULTIPLIER
    try:
        c = x / y
    except ZeroDivisionError:
        c = 0
    return c + random.randint(MIN_RANDOM, MAX_RANDOM) + b


z = 0
for i in range(1, MAX_RANGE + 1):
    z += calc(i, DEFAULT_DIVISOR)

print(f"finished {z}")
