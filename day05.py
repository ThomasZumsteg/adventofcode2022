"""Solution to day 5 for Advent of Code"""

from get_input import get_input
from copy import deepcopy
from itertools import takewhile, count
import re


def part1(stack_instructions):
    stacks, instructions = stack_instructions
    stacks = deepcopy(stacks)
    for (cnt, frm, to) in instructions:
        for _ in range(cnt):
            stacks[to].append(stacks[frm].pop())
    return ''.join(stacks[s][-1] for s in sorted(stacks.keys()))


def part2(stack_instructions):
    stacks, instructions = stack_instructions
    stacks = deepcopy(stacks)
    for (cnt, frm, to) in instructions:
        stacks[to].extend(stacks[frm][-cnt:])
        stacks[frm][-cnt:] = []
    return ''.join(stacks[s][-1] for s in sorted(stacks.keys()))


def parse(text):
    crate_lines = []
    lines = iter(text.strip().split("\n"))
    for line in takewhile(lambda line: line != "", lines):
        crate_lines.append(line)
    cols = [int(n) for n in crate_lines[-1].strip().split(' ') if n != '']
    crates = {c: [] for c in cols}
    for line in crate_lines[:-1]:
        for i, key in zip(count(1, 4), cols):
            if line[i] == " ":
                continue
            assert 'A' <= line[i] <= 'Z'
            crates[key].insert(0, line[i])
    instructions = []
    move_re = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
    for line in lines:
        m = move_re.match(line)
        instructions.append(tuple(int(g) for g in m.groups()))
    return (crates, instructions)


if __name__ == "__main__":
    LINES = parse(get_input(day=5, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
