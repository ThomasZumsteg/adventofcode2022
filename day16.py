"""Solution to day 15 for Advent of Code"""

from get_input import get_input, line_parser
from functools import cache
import re


class Valves:
    def __init__(self, lines):
        self.valves = {name: (flow_rate, tuple(connected))
                       for (name, flow_rate, connected) in lines}
        self.unstuck = set(
            name for name, flow_rate, _
            in lines if flow_rate > 0
        )
        self.unstuck.add('AA')
        self.connections = {}
        for valve in self.unstuck:
            self.connections[valve] = {}
            seen = set()
            queue = [(valve, 0)]
            while queue:
                pos, steps = queue.pop(0)
                if pos in seen:
                    continue
                seen.add(pos)
                if pos in self.unstuck and pos != valve\
                        and pos not in self.connections[valve] and pos != 'AA':
                    self.connections[valve][pos] = steps
                queue.extend((p, steps+1) for p in self.valves[pos][1])

    def get_paths(self, location, budget, exclude=None):
        if exclude is None:
            exclude = set()
        if budget >= 1:
            yield (location, )
        for dest, cost in self.connections[location].items():
            if dest in exclude:
                continue
            if budget >= cost + 2:
                for path in self.get_paths(dest, budget - cost - 1, exclude | {location}):  # noqa
                    yield (location, ) + path

    @cache
    def value(self, path, time):
        result = 0
        for src, dest in zip(path, path[1:]):
            time -= self.connections[src][dest] + 1
            result += time * self.valves[dest][0]
        return result


def part1(lines):
    valves = {name: (flow_rate, tuple(connected))
              for (name, flow_rate, connected) in lines}
    valves = Valves(lines)
    best = 0
    for path in valves.get_paths('AA', 30):
        best = max(best, valves.value(path, 30))
    return best


def part2(lines):
    valves = Valves(lines)
    best = 0
    for path1 in valves.get_paths("AA", 26, None):
        for path2 in valves.get_paths("AA", 26, exclude=set(path1)):
            best = max(best, valves.value(path1, 26) + valves.value(path2, 26))
    return best


def parse(line):
    m = re.match(
        r"Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$",
        line
    )
    return (m.group(1), int(m.group(2)), [t for t in m.group(3).split(', ')])


TEST = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

if __name__ == "__main__":
    assert part1(line_parser(TEST, parse=parse)) == 1651
    assert part2(line_parser(TEST, parse=parse)) == 1707
    LINES = line_parser(get_input(day=16, year=2022), parse=parse)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
