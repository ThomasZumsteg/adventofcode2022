"""Solution to day 23 for Advent of Code"""

from get_input import get_input
from collections import defaultdict
from itertools import count


def show_board(board):
    result = []
    rows = sorted(int(p.real) for p in board)
    cols = sorted(int(p.imag) for p in board)
    for r in range(rows[0], rows[-1]+1):
        line = []
        for c in range(cols[0], cols[-1]+1):
            char = '.'
            if complex(r, c) in board:
                if isinstance(board, dict):
                    char = str(len(board[complex(r, c)]))
                else:
                    char = '#'
            line.append(char)
        result.append(''.join(line))
    return '\n'.join(result)


def boards(elves):
    moves = [
        (-1+0j, -1+1j, -1-1j),  # North: N, NE, NW
        (1+0j, 1+1j, 1-1j),  # South: S, SE, SW
        (0-1j, 1-1j, -1-1j),  # West: W, NW, SW
        (0+1j, 1+1j, -1+1j),  # East: E, NE, SE
    ]
    while True:
        proposed = defaultdict(set)
        for elf in elves:
            if all(elf+m not in elves for move in moves for m in move):
                # Stay put if there's no other elves
                proposed[elf].add(elf)
                continue
            for checks in moves:
                if any(elf+check in elves for check in checks):
                    continue
                proposed[elf+checks[0]].add(elf)
                break
            else:
                # If there's no moves, also stay put
                proposed[elf].add(elf)
        elves = set()
        for target, elf in proposed.items():
            if len(elf) == 1:
                elves.add(target)
            else:
                elves.update(elf)
        yield elves
        moves.append(moves.pop(0))


def part1(elves):
    for r, board in enumerate(boards(elves), 1):
        if r >= 10:
            rows = sorted(int(p.real) for p in board)
            cols = sorted(int(p.imag) for p in board)
            return (rows[-1]-rows[0]+1) * (cols[-1]-cols[0]+1) - len(board)


def part2(elves):
    old = elves
    for r, new in enumerate(boards(elves), 1):
        if old == new:
            return r
        old = new


def parse(text):
    elves = set()
    for r, row in enumerate(text.strip().split("\n")):
        for c, char in enumerate(row):
            if char == '#':
                elves.add(complex(r, c))
            else:
                assert char == '.'
    return elves


TEST = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""


if __name__ == "__main__":
    assert part1(parse(TEST)) == 110
    assert part2(parse(TEST)) == 20
    LINES = parse(get_input(day=23, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
