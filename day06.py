"""Solution to day 6 for Advent of Code"""

from get_input import get_input


def part1(datastream, bufsize=4):
    buffer = []
    for c, char in enumerate(datastream, 1):
        buffer.append(char)
        if len(buffer) < bufsize:
            continue
        if len(buffer) > bufsize:
            buffer.pop(0)
        if len(set(buffer)) == bufsize:  # There's a duplicate somewhere
            return c
    raise NotImplementedError()


def part2(datastream):
    return part1(datastream, bufsize=14)


if __name__ == "__main__":
    assert part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    LINES = get_input(day=6, year=2022)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
