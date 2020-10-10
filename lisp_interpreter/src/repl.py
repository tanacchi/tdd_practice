def tokenize(source):
    try:
        return int(source)
    except ValueError:
        return source


def parse(source):
    return source


def read():
    source_str = input("> ")
    return parse(source_str)


def evaluate(src):
    if not isinstance(src, list):
        return src
    elif src[0] == '+':
        return src[1] + src[2]
    else:
        return src[1] - src[2]


if __name__ == '__main__':
    while True:
        result = evaluate(read())

        print("-" * 10)
        print("  {}  <{}>".format(result, type(result).__name__))
        print("-" * 10)
        print()
