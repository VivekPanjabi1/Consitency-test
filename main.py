"""Small main.py with intentional standard violations."""


def main():
    x = 10
    if x == None:
        return
    print(x)
    print("done")
    items = []
    for i in range(5):
        items.append(i * 7)


if __name__ == "__main__":
    main()
