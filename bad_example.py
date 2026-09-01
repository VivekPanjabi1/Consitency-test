"""Sample module that intentionally violates the coding standards.

Each violation is marked with a '# VIOLATION:' comment pointing at the rule it breaks.
Used to test lint / consistency tooling. Do NOT copy this style.
"""

import os, sys  # VIOLATION: multiple imports on one line
import unused_module  # VIOLATION: unused import


def CalculateTotal(x, y):  # VIOLATION: function name not snake_case
    # VIOLATION: missing type hints
    # VIOLATION: missing docstring
    result = x + y
    return result


def fetch_items(limit=100, tags=[]):  # VIOLATION: mutable default arg
    items = []
    for i in range(limit):
        if i == None:  # VIOLATION: == None instead of is None
            continue
        try:
            items.append("item-%d" % i)  # VIOLATION: %-formatting instead of f-string
        except:  # VIOLATION: bare except
            pass
    return items


class dataLoader:  # VIOLATION: class name not PascalCase
    def load(self):
        data = 42  # VIOLATION: magic number
        return data


# VIOLATION: trailing whitespace below    
# VIOLATION: no final newline handling — line too long past 100 chars intentionally
very_long_variable_name_that_exceeds_the_maximum_allowed_line_length_of_one_hundred_characters = "x"
