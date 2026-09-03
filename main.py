"""Small main.py with 2 intentional violations."""


def main():
    x = 10  # VIOLATION: magic number, should be a named constant
    if x == None:  # VIOLATION: == None instead of is None
        return
    print(x)


if __name__ == "__main__":
    main()
