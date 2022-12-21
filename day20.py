"""Solution to day 20 for Advent of Code"""

from get_input import get_input, line_parser
from dataclasses import dataclass, field


@dataclass
class Link:
    number: int
    before: field(init=False) = None
    after: field(init=False) = None

    def __repr__(self):
        before = self.before.number if self.before is not None else None
        after = self.after.number if self.after is not None else None
        return f"Link({self.number}, {before}, {after})"

    def nth(self, nth, limit):
        nth %= limit
        assert nth >= 0
        node = self
        for _ in range(nth):
            node = node.after
        return node

    def pop(self):
        self.before.after, self.after.before = self.after, self.before
        self.before = self.after = None
        return self

    def insert_after(self, node):
        node.before, node.after = self, self.after
        node.before.after = node.after.before = node

    def as_list(self):
        items = [self.number]
        node = self.after
        while node != self:
            items.append(node.number)
            node = node.after
        return items


def part1(numbers, key=1, count=1):
    current = None
    elements = []
    for n in numbers:
        current = Link(key*n, current)
        elements.append(current)
        if current.before is not None:
            current.before.after = current
        else:
            first = current
        if n == 0:
            root = current
    current.after, first.before = first, current
    size = len(numbers)
    for _ in range(count):
        for element in elements:
            node = element.nth(element.number, limit=(size-1))
            if node != element:
                element = element.pop()
                node.insert_after(element)
    return sum(root.nth(n, limit=size).number for n in (1000, 2000, 3000))


def part2(numbers):
    return part1(numbers, key=811589153, count=10)


TEST = """1
2
-3
3
-2
0
4"""

if __name__ == "__main__":
    assert part1(line_parser(TEST, parse=int)) == 3
    assert part2(line_parser(TEST, parse=int)) == 1623178306
    LINES = line_parser(get_input(day=20, year=2022), parse=int)
    # 285 is to low
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
