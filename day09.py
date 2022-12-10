"""Solution to day 9 for Advent of Code"""

from get_input import get_input, line_parser


def part1(items, num_knots=2):
    knots = [0+0j] * num_knots

    visited = set([knots[-1]])
    for move, distace in items:
        for _ in range(distace):
            knots[0] += move

            for i in range(num_knots-1):
                diff = knots[i] - knots[i+1]
                if diff.real == 0 and abs(diff.imag) > 1:
                    # move in imag
                    knots[i+1] += complex(0, abs(diff.imag) / diff.imag)
                elif abs(diff.real) > 1 and diff.imag == 0:
                    # move in real
                    knots[i+1] += complex(abs(diff.real) / diff.real, 0)
                elif abs(diff) > 2**0.5:
                    # move diagonally
                    knots[i+1] += complex(
                        abs(diff.real) / diff.real,
                        abs(diff.imag) / diff.imag
                    )
            visited.add(knots[-1])
    return len(visited)


def part2(items):
    return part1(items, num_knots=10)


def parse(line):
    move_map = {
        "L": 0-1j,
        "R": 0+1j,
        "U": -1+0j,
        "D": 1+0j,
    }
    fields = line.split(" ")
    return (move_map[fields[0]], int(fields[1]))


TEST = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


TEST2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

if __name__ == "__main__":
    assert part1(line_parser(TEST, parse=parse)) == 13
    assert part2(line_parser(TEST2, parse=parse)) == 36
    LINES = line_parser(get_input(day=9, year=2022), parse=parse)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
