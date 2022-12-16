"""Solution to day 15 for Advent of Code"""

from get_input import get_input, line_parser
import re


def get_segments(squares, target):
    square_segments = []
    for (center, beacon) in squares:
        diff = center - beacon
        length = abs(diff.real) + abs(diff.imag) - abs(target - center.imag)
        if 0 < length:
            square_segments.append((
                center.real - length,
                center.real + length))
    square_segments.sort()
    segments = [square_segments[0]]
    for segment in square_segments[1:]:
        last = segments.pop()
        assert last[0] <= segment[0]
        if last[1] + 1 < segment[0]:
            segments.append(last)
        else:
            segment = (min(last[0], segment[0]), max(last[1], segment[1]))
        segments.append(segment)
    return segments


def part1(squares, target=2000000):
    segments = get_segments(squares, target)
    return int(sum(start - end for end, start in segments))


def part2(squares, rows=4_000_000):
    for row in range(rows+1):
        print(row, end='\r')
        segments = get_segments(squares, row)
        if len(segments) != 1:
            assert len(segments) == 2
            first = segments[0][1]
            second = segments[1][0]
            assert first + 2 == second
            print(' ' * 20, end='\r')
            return 4_000_000 * int(first + 1) + row
    raise NotImplementedError()


def parse(line):
    match = re.match(
        r'Sensor at x=(-?\d+), y=(-?\d+): '
        r'closest beacon is at x=(-?\d+), y=(-?\d+)',
        line)
    return (complex(int(match.group(1)), int(match.group(2))),
            complex(int(match.group(3)), int(match.group(4))))


TEST = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

if __name__ == "__main__":
    assert part1(line_parser(TEST, parse=parse), target=10) == 26
    assert part2(line_parser(TEST, parse=parse), rows=20) == 56000011
    LINES = line_parser(get_input(day=15, year=2022), parse=parse)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
