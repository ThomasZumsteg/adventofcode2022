"""Solution to day 8 for Advent of Code"""

from get_input import get_input
from itertools import chain


def part1(trees):
    max_row = max(int(p.real) for p in trees.keys())
    max_col = max(int(p.imag) for p in trees.keys())
    queue = [(point, step, trees[point]) for (point, step) in chain(
        ((complex(0, c), 1+0j) for c in range(max_col+1)),
        ((complex(max_row, c), -1+0j) for c in range(max_col+1)),
        ((complex(r, 0), 0+1j) for r in range(max_row+1)),
        ((complex(r, max_col), 0-1j) for r in range(max_row+1)),
    )]
    tallest = set(p[0] for p in queue)
    while queue:
        point, step, height = queue.pop()
        point += step
        if point not in trees:
            continue
        if trees[point] > height:
            tallest.add(point)
            height = trees[point]
        queue.append((point, step, height))
    return len(tallest)


def part2(trees):
    max_score = 0
    for tree, height in trees.items():
        score = 1
        for step in (-1+0j, 0-1j, 1+0j, 0+1j):
            steps = 0
            point = tree + step
            while point in trees:
                steps += 1
                if trees[point] >= height:
                    break
                point += step
            score *= steps
        max_score = max(max_score, score)
    return max_score


def parse(lines):
    trees = {}
    for r, row in enumerate(lines.strip().split('\n')):
        for c, val in enumerate(row):
            trees[complex(r, c)] = int(val)
    return trees


TEST = """30373
25512
65332
33549
35390"""


if __name__ == "__main__":
    assert part1(parse(TEST)) == 21, part1(parse(TEST))
    assert part2(parse(TEST)) == 8
    LINES = parse(get_input(day=8, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
