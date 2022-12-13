"""Solution to day 11 for Advent of Code"""

from functools import reduce
from get_input import get_input
from itertools import groupby
from operator import mul
import re


class Monkey:
    def __init__(self, name, items, update, test, actions):
        self.name = name
        self.items = items.copy()
        if not callable(update):
            update = self.make_update(*update)
        self.update = update
        self.test = test
        self.actions = actions
        self.counted = 0

    def clone(self):
        return Monkey(self.name, self.items, self.update, self.test, self.actions)

    @staticmethod
    def make_update(op, value):
        if op == "+" and value != "old":
            return lambda v: v + int(value)
        elif op == "*" and value != "old":
            return lambda v: v * int(value)
        elif op == "+" and value == "old":
            return lambda v: v * 2
        elif op == "*" and value == "old":
            return lambda v: int(v ** 2)
        else:
            raise NotImplementedError()

    def inspect(self, destress=lambda v: v // 3):
        while self.items != []:
            item = self.items.pop(0)
            item = destress(self.update(item))
            self.counted += 1
            yield (self.actions[item % self.test == 0], item)

    def __repr__(self):
        return f"{self.name}: [{' ,'.join(str(i) for i in self.items)}]"


def part1(monkeys):
    monkeys = {m.name: m.clone() for m in monkeys}
    for _ in range(20):
        for monkey in monkeys.values():
            for move_to, item in monkey.inspect():
                # print(f"{monkey} ({item}) -> {move_to}")
                monkeys[move_to].items.append(item)
    scores = sorted((m.counted for m in monkeys.values()), reverse=True)
    return scores[0] * scores[1]


def part2(monkeys):
    monkeys = {m.name: m.clone() for m in monkeys}
    lcm = reduce(mul, (m.test for m in monkeys.values()), 1)
    destress = lambda v: v % lcm
    for rnd in range(10_000):
        for monkey in monkeys.values():
            for move_to, item in monkey.inspect(destress=destress):
                monkeys[move_to].items.append(item)
    scores = sorted((m.counted for m in monkeys.values()), reverse=True)
    return scores[0] * scores[1]


def parse(lines):
    lines = iter(lines.strip().split("\n"))
    monkey_match = re.compile(
        r'Monkey (?P<name>\d+):\n'
        r'  Starting items: (?P<items>.*)\n'
        r'  Operation: new = old (?P<op_type>\*|\+) (?P<op_value>\d+|old)\n'
        r'  Test: divisible by (?P<test_value>\d+)\n'
        r'    If true: throw to monkey (?P<if_true>\d+)\n'
        r'    If false: throw to monkey (?P<if_false>\d+)\n?'
    )
    monkeys = []
    for _, group in groupby(enumerate(lines), lambda nl: nl[0] // 7):
        text = "\n".join(l for _, l in group)
        m = monkey_match.match(text)
        monkey = Monkey(
            name=int(m.group('name')),
            items=list(int(n) for n in m.group('items').split(', ')),
            update=(m.group('op_type'), m.group('op_value')),
            test=int(m.group('test_value')),
            actions={
                True: int(m.group('if_true')),
                False: int(m.group('if_false'))
            }
        )
        monkeys.append(monkey)
    return monkeys


TEST = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

if __name__ == "__main__":
    assert part1(parse(TEST)) == 10605
    assert part2(parse(TEST)) == 2713310158
    LINES = parse(get_input(day=11, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
