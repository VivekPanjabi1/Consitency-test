"""Small sample violating the coding standards. Each break is marked '# VIOLATION:'."""

import os  # VIOLATION: unused import


def Add(a, b):  # VIOLATION: not snake_case, no type hints, no docstring
    return a + b


def get_data(items=[]):  # VIOLATION: mutable default arg
    result = []
    for x in items:
        if x == None:  # VIOLATION: == None instead of is None
            continue
        try:
            result.append("%s" % x)  # VIOLATION: %-format instead of f-string
        except:  # VIOLATION: bare except
            pass
    return result


MAX = 100  # VIOLATION: constant not UPPER_SNAKE (should be fine) — actually ok, but used as magic below
total = Add(5, MAX)  # VIOLATION: magic number 5
