def convert(input_str):
    val = 0
    prev = None
    for c in input_str:
        if c == "I":
            val += 1
        elif c == "V":
            val += 3 if prev == "I" else 5
        else:
            raise ValueError(f"Invalid character {c}.")
        prev = c
    return val
