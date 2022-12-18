"""Solution to day 17 for Advent of Code"""

from get_input import get_input
from itertools import cycle, product
from collections import defaultdict


ROCKS = (
    # '####',
    (0+0j, 0+1j, 0+2j, 0+3j),
    # '.#.'
    # '###'
    # '.#.',
    (0+1j, 1+0j, 1+1j, 1+2j, 2+1j),
    # '..#'
    # '..#'
    # '###',
    (0+0j, 0+1j, 0+2j, 1+2j, 2+2j),
    # '#'
    # '#'
    # '#'
    # '#',
    (0+0j, 1+0j, 2+0j, 3+0j),
    # '##'
    # '##'
    (0+0j, 0+1j, 1+0j, 1+1j),
)


def part1(moves, goal=2022):
    moves = cycle(enumerate(iter(moves)))
    board = {}
    seen = defaultdict(list)
    top = 0
    heights = [top]

    for n, (r, rock) in enumerate(cycle(enumerate(ROCKS)), 1):
        if n > goal:
            break
        step_down = [r + complex(top + 4, 2) for r in rock]
        while not any(r in board or r.real <= 0 for r in step_down):
            rock = step_down
            m, move = next(moves)
            diff = {'<': 0-1j, '>': 0+1j}[move]
            step = [r + diff for r in rock]
            if all(0 <= s.imag <= 6 and s not in board for s in step):
                rock = step
            step_down = [r + -1+0j for r in rock]
        board.update((r, '#') for r in rock)
        top = max(top, max(r.real for r in rock))
        heights.append(top)

        top_n = frozenset(
            complex(r, c) for r, c in product(range(10), range(7))
            if complex(top - r, c) in board
        )

        key = (m, r, top_n)
        if len(seen[key]) > 1:  # step size should be consistent
            step_size = set(b - a for a, b in zip(seen[key], seen[key][1:]))
            assert len(step_size) == 1
            step_size = step_size.pop()
            start = seen[key][0]
            steps, rem = divmod(goal - start, step_size)

            before = heights[start]
            skipped = steps * (heights[start + step_size] - heights[start])
            after = heights[start + rem] - heights[start]
            return int(before + skipped + after)
        seen[key].append(n)
    return int(heights[-1])


def part2(moves):
    return part1(moves, goal=1000000000000)


TEST = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

if __name__ == "__main__":
    assert part1(list(TEST)) == 3068
    assert part2(list(TEST)) == 1514285714288, part2(list(TEST))
    LINES = list(get_input(day=17, year=2022).strip())
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
