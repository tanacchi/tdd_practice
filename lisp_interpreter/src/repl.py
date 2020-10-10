def tokenize(source):
    try:
        return int(source)
    except ValueError:
        return source


def read():
    source_str = input("> ")
    return tokenize(source_str)


def evaluate(src):
    if not isinstance(src, list):
        return src
    return src[1] + src[2]


if __name__ == '__main__':
    while True:
        result = evaluate(read())

        print("-" * 10)
        print("  {}  <{}>".format(result, type(result).__name__))
        print("-" * 10)
        print()
