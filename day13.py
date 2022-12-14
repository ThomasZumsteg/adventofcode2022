"""Solution to day 13 for Advent of Code"""

from get_input import get_input, line_parser
from functools import cmp_to_key


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        return 0
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    for (l, r) in zip(left, right):
        result = compare(l, r)
        if result != 0:
            return result
    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    return 0


def part1(pairs):
    return sum(i for i, (left, right) in enumerate(pairs, 1)
               if compare(left, right) != 1)


def part2(pairs):
    items = sorted([i for p in pairs + [([[2]], [[6]])] for i in p],
                   key=cmp_to_key(compare))
    return (items.index([[2]]) + 1) * (items.index([[6]]) + 1)


def parse(pairs):
    return tuple(eval(p) for p in pairs.strip().split('\n'))


TEST = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

if __name__ == "__main__":
    # assert part1(line_parser(TEST, seperator='\n\n', parse=parse)) == 13
    assert part2(line_parser(TEST, seperator='\n\n', parse=parse)) == 140
    LINES = line_parser(get_input(day=13, year=2022), seperator='\n\n', parse=parse)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
