def read():
    return input("> ")


def evaluate(src):
    return src


if __name__ == '__main__':
    while True:
        result = evaluate(read())

        print("-"*10)
        print("  {}  <{}>".format(result, type(result).__name__))
        print("-"*10)
        print()
