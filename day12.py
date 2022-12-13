"""Solution to day 12 for Advent of Code"""

from get_input import get_input


def part1(height_map, start=ord('a')-1):
    queue = [(0, k) for k, v in height_map.items() if v <= start]
    seen = set()
    while queue:
        steps, location = queue.pop(0)
        if location in seen:
            continue
        seen.add(location)
        current = height_map[location]
        if current == ord('z') + 1:
            return steps

        for direction in (0+1j, 0-1j, 1+0j, -1+0j):
            step = direction + location
            if step not in height_map or height_map[step] - current > 1:
                continue
            queue.append((steps+1, step))
    raise NotImplementedError()


def part2(height_map):
    return part1(height_map, start=ord('a'))


def parse(text):
    height_map = {}
    for r, row in enumerate(text.strip().split("\n")):
        for c, char in enumerate(row):
            if char == 'S':
                char = chr(ord('a') - 1)
            elif char == 'E':
                char = chr(ord('z') + 1)
            height_map[complex(r, c)] = ord(char)
    return height_map


TEST = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


if __name__ == "__main__":
    assert part1(parse(TEST)) == 31
    assert part2(parse(TEST)) == 29
    LINES = parse(get_input(day=12, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
