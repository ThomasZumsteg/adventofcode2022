"""Solution to day 21 for Advent of Code"""

from get_input import get_input
from operator import sub, add, mul, floordiv


FUNCS = {
    # a + b = v, v - b = a, v - a = b
    '+': (add, sub, sub),
    # a - b = v: v + b = a, a - v = b
    '-': (sub, add, lambda v, a: a - v),
    # a * b = v: v / b = a, v / a = b
    '*': (mul, floordiv, floordiv),
    # a / b = v: v * b = a, a / v = b
    '/': (floordiv, mul, lambda v, a: a // v),
}


def get_value_func(monkeys):

    def wrapped(monkey, match=None):
        if match is not None and monkey not in monkeys:
            assert monkey == 'humn'
            monkeys[monkey] = match
        value = monkeys.get(monkey)

        if isinstance(value, int) or value is None:
            return value

        a, f, b = value

        value_a, value_b = wrapped(a), wrapped(b)
        if (value_a is None or value_b is None) and match is None:
            return None
        if value_a is None:
            value_a = wrapped(a, match=FUNCS[f][1](match, value_b))
        if value_b is None:
            value_b = wrapped(b, match=FUNCS[f][2](match, value_a))
        return FUNCS[f][0](value_a, value_b)

    return wrapped


def part1(monkeys):
    get_value = get_value_func(monkeys)
    return get_value("root")


def part2(monkeys):
    monkeys = monkeys.copy()
    del monkeys['humn']
    get_value = get_value_func(monkeys)

    monkey_a, _, monkey_b = monkeys['root']
    value = get_value(monkey_b)
    get_value(monkey_a, match=value)

    return monkeys['humn']


def parse(lines):
    monkeys = {}
    for line in lines.strip().split('\n'):
        name, remain = line.split(': ', 1)
        if remain.isdigit():
            content = int(remain)
        else:
            content = tuple(remain.split(' ', 2))
        assert name not in monkeys
        monkeys[name] = content
    return monkeys


TEST = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""


if __name__ == "__main__":
    assert part1(parse(TEST)) == 152
    assert part2(parse(TEST)) == 301
    LINES = parse(get_input(day=21, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
