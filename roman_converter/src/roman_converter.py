import math


convert_map = {
    'I': 1,   'V': 5,
    'X': 10,  'L': 50,
    'C': 100, 'D': 500,
    'M': 1000
}

def convert(input_str):
    val = 0
    prev = math.inf
    for c in input_str:
        try:
            curr = convert_map[c]
            val += curr if curr <= prev else curr - prev * 2
            prev = curr
        except KeyError:
            raise ValueError(f"Invalid character {c}.")
    return val
