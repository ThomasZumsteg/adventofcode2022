"""Solution to day 24 for Advent of Code"""

from get_input import get_input
from collections import defaultdict
from functools import cache
from itertools import count


def show_board(walls, blizzards):
    rows = sorted(int(w.real) for w in walls)
    cols = sorted(int(w.imag) for w in walls)
    dirs = {
        1+0j: 'v',
        -1+0j: '^',
        0+1j: '>',
        0-1j: '<',
    }
    lines = []
    for row in range(rows[0], rows[-1]+1):
        line = []
        for col in range(cols[0], cols[-1]+1):
            point = complex(row, col)
            if point in walls:
                assert point not in blizzards
                line.append('#')
            elif point not in blizzards:
                line.append('.')
            else:
                blizs = blizzards[point]
                if len(blizs) > 1:
                    line.append(str(len(blizs)))
                else:
                    line.append(dirs[next(iter(blizs))])
        lines.append(''.join(line))
    return '\n'.join(lines)


def part1(board, target_trips=1):
    walls = set(p for p, c in board.items() if c == '#')
    blizzards = {p: set([b]) for p, b in board.items()
                 if isinstance(b, complex)}

    @cache
    def move_blizzard(p, b):
        if p+b in walls:
            while p not in walls:
                p -= b
        return p+b

    next_states = [next(complex(0, c) for c in count(0)
                        if complex(0, c) not in walls)]
    last_row = max(p.real for p in walls)
    target_row = last_row
    trips = 0
    for step in count(0):
        next_blizzards = defaultdict(set)
        for p, b in ((p, b) for p, bs in blizzards.items() for b in bs):
            next_blizzards[move_blizzard(p, b)].add(b)
        blizzards = next_blizzards
        states = next_states
        next_states = set()
        for s in states:
            if s.real == target_row:
                trips += 1
                if trips >= target_trips:
                    return step
                target_row = last_row if trips % 2 == 0 else 0
                next_states = set([s])
                break
            for diff in (0+0j, 0+1j, 0-1j, 1+0j, -1+0j):
                point = s+diff
                if point not in walls and point not in blizzards\
                        and 0 <= point.real <= last_row:
                    next_states.add(point)


def part2(board):
    return part1(board, target_trips=3)


def parse(text):
    board = {}
    blizzards = {
        'v': 1+0j,
        '^': -1+0j,
        '>': 0+1j,
        '<': 0-1j,
    }
    for r, row in enumerate(text.strip().split('\n')):
        for c, char in enumerate(row):
            if char == '.':
                continue
            board[complex(r, c)] = blizzards.get(char, char)
    return board


TEST = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

if __name__ == "__main__":
    assert part1(parse(TEST)) == 18
    assert part2(parse(TEST)) == 54
    LINES = parse(get_input(day=24, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
