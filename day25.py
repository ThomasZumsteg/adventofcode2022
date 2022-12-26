"""Solution to day 25 for Advent of Code"""

from get_input import get_input, line_parser
from math import log, ceil

def from_snafu(num):
    values = {
        '=': -2,
        '-': -1,
        '0': 0,
        '1': 1,
        '2': 2,
    }
    total = []
    for char in num:
        total = [5*v for v in total]
        total.append(values[char])
    return sum(total)


def to_snafu(num):
    values = {
        -2: '=',
        -1: '-',
        0: '0',
        1: '1',
        2: '2',
    }
    remainer = num
    digits = []
    for n in reversed(range(0, ceil(log(num)/log(5)))):
        digit = min(range(-2, 3), key=lambda v: abs(remainer - v*5**n))
        remainer -= digit * 5**n
        digits.append(values[digit])
    return ''.join(digits)


def part1(snafus):
    total = sum(from_snafu(snafu) for snafu in snafus)
    return to_snafu(total)


def parse(line):
    raise NotImplementedError()


TEST = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""


if __name__ == "__main__":
    assert part1(line_parser(TEST, parse=str)) == "2=-1=0"
    LINES = line_parser(get_input(day=25, year=2022), parse=str)
    print(f"Part 1: {part1(LINES)}")
