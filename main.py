import random


def calc(x, y):
    a = x + y
    b = a * 2
    try:
        c = x / y
    except:
        c = 0
    return c + random.randint(1, 100) + b


z = 0
for i in range(1, 21):
    z += calc(i, 0)

print("done", z)
