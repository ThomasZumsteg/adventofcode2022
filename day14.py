"""Solution to day 14 for Advent of Code"""

from get_input import get_input


DOWN = 0+1j
LEFT = -1+0j
RIGHT = 1+0j


def part1(rock_map):
    rock_map = rock_map.copy()
    last = max(p.imag for p in rock_map.keys())
    sand = 500+0j
    while True:
        if sand.imag > last:
            return sum(1 for v in rock_map.values() if v == 'o')
        elif (sand + DOWN) not in rock_map:
            # Keep going
            sand += DOWN
        elif (sand + DOWN + LEFT) not in rock_map:
            sand += DOWN + LEFT
        elif (sand + DOWN + RIGHT) not in rock_map:
            sand += DOWN + RIGHT
        else:
            rock_map[sand] = 'o'
            sand = 500+0j
    raise NotImplementedError()


def part2(rock_map):
    rock_map = rock_map.copy()
    last = max(p.imag for p in rock_map.keys())
    sand = 500+0j
    while True:
        if sand == 500+0j and sand in rock_map:
            return sum(1 for v in rock_map.values() if v == 'o')
        elif sand.imag >= last + 1:
            rock_map[sand] = 'o'
            sand = 500+0j
        elif (sand + DOWN) not in rock_map:
            sand += DOWN
        elif (sand + DOWN + LEFT) not in rock_map:
            sand += DOWN + LEFT
        elif (sand + DOWN + RIGHT) not in rock_map:
            sand += DOWN + RIGHT
        else:
            rock_map[sand] = 'o'
            sand = 500+0j
    raise NotImplementedError()


def parse(text):
    rock_map = {}
    for line in text.strip().split('\n'):
        steps = []
        for step in line.split(' -> '):
            r, c = [int(f) for f in step.split(',')]
            steps.append(complex(int(r), int(c)))
        for spot, stop in zip(steps, steps[1:]):
            diff = (stop - spot) / abs(stop - spot)
            while (spot - diff) != stop:
                rock_map[spot] = "#"
                spot += diff
    return rock_map


TEST = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

if __name__ == "__main__":
    assert part1(parse(TEST)) == 24
    assert part2(parse(TEST)) == 93
    LINES = parse(get_input(day=14, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
