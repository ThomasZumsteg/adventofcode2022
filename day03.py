"""Solution to day 3 for Advent of Code"""

from get_input import get_input, line_parser
import string


def score(*sacks):
    common = set.intersection(*list(set(s) for s in sacks))
    assert len(common) == 1
    return string.ascii_letters.index(common.pop()) + 1


def part1(sacks):
    pairs = ((sack[:len(sack) // 2], sack[len(sack) // 2:]) for sack in sacks)
    return sum(score(*pair) for pair in pairs)


def part2(items):
    triples = zip(items[::3], items[1::3], items[2::3])
    return sum(score(*sacks) for sacks in triples)


if __name__ == "__main__":
    LINES = line_parser(get_input(day=3, year=2022), parse=str)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
