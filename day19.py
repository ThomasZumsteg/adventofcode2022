"""Solution to day 18 for Advent of Code"""

from get_input import get_input, line_parser
import functools
from operator import mul
from collections import deque
import re


def value_func(blueprints):
    robots = {
        tuple(blueprint[:4]): tuple(-n for n in blueprint[:4])
        for blueprint in blueprints
    }
    costs = [
        robots[(1, 0, 0, 0)],
        robots[(0, 1, 0, 0)],
        robots[(0, 0, 1, 0)],
        robots[(0, 0, 0, 1)],
    ]

    @functools.cache
    def wrapped(state):
        resources = tuple(state[4:])
        for count, cost in zip(state[:4], costs):
            resources = tuple(r - count*c for r, c in zip(resources, cost))  # noqa
        return resources
    return wrapped


def work(state, time, blueprints):
    max_geode = 0
    queue = deque()
    queue.append((time,) + state)
    seen = set()
    get_value = value_func(blueprints)
    diff = (0, 2, 0, 0)
    best = (0, 0, 0, 0)
    while len(queue) > 0:
        t, *state = queue.popleft()
        state = tuple(state)
        max_geode = max(max_geode, state[4])
        value = get_value(state)
        best = max(best, value)
        if t <= 0 or state in seen or \
                tuple(v+d for v, d in zip(value, diff)) < best:
            continue
        seen.add(state)

        resources = (0, 0, 0, 0) + state[:4]
        for n, blueprint in enumerate(blueprints):
            if all(b + s >= 0 for b, s in zip(blueprint[4:], state[4:])):
                new_state = tuple(s+r+b for s, r, b in zip(
                    state, resources, blueprint,))
                queue.append((t-1,) + new_state)
    return max_geode


def part1(blueprints):
    state = (0, 0, 0, 1, 0, 0, 0, 0)
    partial = functools.partial(work, state, 24)
    result = {b['id']: partial(b['changes']) for b in blueprints}
    return sum(k * v for k, v in result.items())


def part2(blueprints):
    blueprints = blueprints[:3]
    state = (0, 0, 0, 1, 0, 0, 0, 0)
    partial = functools.partial(work, state, 32)
    results = [partial(b['changes']) for b in blueprints]
    return functools.reduce(mul, results, 1)


def parse(line):
    m = re.match(
        r'Blueprint (\d+):\n? +'
        r'Each ore robot costs (\d+) ore.\n? +'
        r'Each clay robot costs (\d+) ore.\n? +'
        r'Each obsidian robot costs (\d+) ore and (\d+) clay.\n? +'
        r'Each geode robot costs (\d+) ore and (\d+) obsidian.',
        line)
    return {
        'id': int(m.group(1)),
        'changes': [
            (1, 0, 0, 0, 0, -int(m.group(7)), 0, -int(m.group(6))),
            (0, 1, 0, 0, 0, 0, -int(m.group(5)), -int(m.group(4))),
            (0, 0, 1, 0, 0, 0, 0, -int(m.group(3))),
            (0, 0, 0, 1, 0, 0, 0, -int(m.group(2))),
            (0, 0, 0, 0, 0, 0, 0, 0),
        ]
    }


TEST = """Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian. """

if __name__ == "__main__":
    assert part1(line_parser(TEST, parse=parse, seperator='\n\n')) == 33
    # assert part2(line_parser(TEST, parse=parse)) == 58
    LINES = line_parser(get_input(day=19, year=2022), parse=parse)
    # 285 is to low
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
