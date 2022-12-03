"""Solution to day 2 for Advent of Code"""

from get_input import get_input, line_parser


HANDS = 'ROCK PAPER SCISSORS'.split(' ')


def part1(guide):
    elf_hands = dict(zip("ABC", HANDS))
    my_hands = dict(zip("XYZ", HANDS))
    scores = dict(zip(HANDS, range(1, 4)))
    win = dict(zip(HANDS, HANDS[1:] + HANDS[:1]))

    total = 0
    for elf, me in ((elf_hands[e], my_hands[m]) for (e, m) in guide):
        total += scores[me]
        if win[elf] == me:
            total += 6
        elif elf == me:
            total += 3
    return total


def part2(guide):
    elf_hands = dict(zip("ABC", HANDS))
    scores = dict(zip(HANDS, range(1, 4)))
    win = dict(zip(HANDS, HANDS[1:] + HANDS[:1]))
    loss = dict(zip(HANDS, HANDS[-1:] + HANDS[:-1]))
    total = 0
    for (elf, me) in guide:
        elf = elf_hands[elf]
        if me == 'X':
            me = loss[elf]
        elif me == 'Y':
            total += 3
            me = elf
        elif me == 'Z':
            total += 6
            me = win[elf]
        total += scores[me]
    return total


if __name__ == "__main__":
    LINES = line_parser(get_input(day=2, year=2022),
                        parse=lambda line: line.split())
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
