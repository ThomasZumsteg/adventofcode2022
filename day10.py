"""Solution to day 10 for Advent of Code"""

from get_input import get_input, line_parser


def part1(instructions):
    x = 1
    cycles = 0
    strength = 0
    for instruction in instructions:
        if instruction[0] == "noop":
            count = 1
        else:
            assert instruction[0] == "addx"
            count = 2
        for _ in range(count):
            cycles += 1
            if cycles >= 20 and (cycles-20) % 40 == 0:
                strength += x * cycles
        if instruction[0] == "addx":
            x += int(instruction[1])
    return strength


def part2(instructions):
    x = 1
    cycles = 0
    lines = [[]]
    for instruction in instructions:
        count = 1
        if instruction[0] != "noop":
            count = 2
        for _ in range(count):
            position = cycles % 40
            if abs(x - position) <= 1:
                lines[-1].append("#")
            else:
                lines[-1].append(".")
            if (cycles + 1) % 40 == 0:
                lines.append([])
            cycles += 1
        if instruction[0] == "addx":
            x += int(instruction[1])
    lines.pop()
    return "\n" + "\n".join(''.join(line) for line in lines)


def parse(line):
    return tuple(line.split(' '))


TEST = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


if __name__ == "__main__":
    assert part1(line_parser(TEST, parse=parse)) == 13140
    LINES = line_parser(get_input(day=10, year=2022), parse=parse)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
