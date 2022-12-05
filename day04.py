"""Solution to day 4 for Advent of Code"""

from get_input import get_input, line_parser


def part1(ranges):
    return sum(1 for (f_start, f_end, s_start, s_end) in ranges
               if (s_start <= f_start and f_end <= s_end) or
                  (f_start <= s_start and s_end <= f_end))


def part2(ranges):
    return sum(1 for (f_start, f_end, s_start, s_end) in ranges
               if not (f_end < s_start or s_end < f_start))


def parse(line):
    return tuple(int(n) for part in line.split(',') for n in part.split('-'))


if __name__ == "__main__":
    LINES = line_parser(get_input(day=4, year=2022), parse=parse)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
