"""Solution to day 1 for Advent of Code"""

from get_input import get_input


def part1(elves):
    return max(sum(elf) for elf in elves)


def part2(elves):
    return sum(sorted([sum(elf) for elf in elves])[-3:])


def parse(text):
    return [
        [int(n) for n in group.split("\n")]
        for group in text.strip().split("\n\n")
    ]


if __name__ == "__main__":
    LINES = parse(get_input(day=1, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
