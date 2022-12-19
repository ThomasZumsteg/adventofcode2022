"""Solution to day 18 for Advent of Code"""

from get_input import get_input, line_parser
from dataclasses import dataclass
from itertools import product, chain


@dataclass
class Droplet:
    x: int
    y: int
    z: int

    @classmethod
    def from_line(cls, line):
        x, y, z = [int(n) for n in line.strip().split(',')]
        return cls(x, y, z)

    def __add__(self, other):
        assert isinstance(other, type(self))
        return type(self)(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        return self + other

    def __eq__(self, other):
        assert isinstance(other, type(self))
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"Droplet({self.x}, {self.y}, {self.z})"

    def __lt__(self, other):
        assert isinstance(other, type(self))
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __gt__(self, other):
        assert isinstance(other, type(self))
        return self.x > other.x and self.y > other.y and self.z > other.z

    @classmethod
    def directions(cls):
        yield from iter((
            Droplet(0, 0, 1),
            Droplet(0, 0, -1),
            Droplet(0, 1, 0),
            Droplet(0, -1, 0),
            Droplet(1, 0, 0),
            Droplet(-1, 0, 0),
        ))


def part1(droplets):
    droplets = set(droplets)
    total = 0
    for droplet in droplets:
        for diff in Droplet.directions():
            diff += droplet
            if diff not in droplets:
                total += 1
    return total


def part2(droplets):
    droplets = set(droplets)

    xs = sorted(d.x for d in droplets)
    ys = sorted(d.y for d in droplets)
    zs = sorted(d.z for d in droplets)

    outside = set()
    smallest = Droplet(xs[0]-1, ys[0]-1, zs[0]-1)
    biggest = Droplet(xs[-1]+1, ys[-1]+1, zs[-1]+1)
    queue = [Droplet(x, y, z) for x, y, z in chain(
        product(range(xs[0], xs[-1]), range(ys[0], ys[-1]), (zs[0]-1, zs[-1]+1)),
        product(range(xs[0], xs[-1]), (ys[0]-1, ys[-1]+1), range(zs[0], zs[-1])),
        product((xs[0]-1, xs[-1]+1), range(ys[0], ys[-1]), range(zs[0], zs[-1]))
    )]
    assert all(o not in droplets for o in outside)
    total = 0
    while queue:
        point = queue.pop(0)
        if point in outside:
            continue
        assert point not in droplets
        outside.add(point)
        for step in Droplet.directions():
            step += point
            if not (smallest < step < biggest) or step in outside:
                continue
            if step in droplets:
                total += 1
            else:
                queue.append(step)
    return total


TEST = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

if __name__ == "__main__":
    assert part1(line_parser(TEST, parse=Droplet.from_line)) == 64
    assert part2(line_parser(TEST, parse=Droplet.from_line)) == 58
    LINES = line_parser(get_input(day=18, year=2022), parse=Droplet.from_line)
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
