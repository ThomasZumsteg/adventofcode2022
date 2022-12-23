"""Solution to day 22 for Advent of Code"""

from get_input import get_input, line_parser
import re


def part1(items):
    board, directions = items
    left, right = 0, max(p.imag+1 for p in board)
    up, down = 0, max(p.real+1 for p in board)
    pos = 1+1j
    heading = 0+1j
    while board.get(pos) != '.':
        pos += heading
    for d, direction in enumerate(directions):
        if direction == 'L':
            # 0+1j -> -1+0j -> 0-1j -> 1+0j
            heading = complex(-heading.imag, heading.real)
            continue
        elif direction == 'R':
            # 0+1j -> 1+0j -> 0-1j -> 1+0j
            heading = complex(heading.imag, -heading.real)
            continue
        assert isinstance(direction, int)
        for _ in range(direction):
            step = pos + heading
            while board.get(step) is None:
                if step.real < up:
                    step = complex(down, step.imag)
                elif down < step.real:
                    step = complex(up, step.imag)
                elif step.imag < left:
                    step = complex(step.real, right)
                elif right < step.imag:
                    step = complex(step.real, left)
                else:
                    step += heading
            if board[step] == '#':
                break
            assert board[step] == '.'
            pos = step
    headings = (0+1j, 1+0j, 0-1j, -1+0j)
    return int(1000 * int(pos.real) + 4 * int(pos.imag) + headings.index(heading))  # noqa:E501


def part2(items, test=False):
    board, directions = items
    alt = {}
    if test:
        side = max(p.real for p in board) // 3
        for c in range(1, int(side)+1):
            """
                  111
                  111
                  111
            222333444
            222333444
            222333444
            222333444
                  555666
                  555666
                  555666
            """
            # map 1<->2
            alt[(complex(0, 2*side+c), (-1+0j))] = (complex(side+1, side+1-c), (1+0j))  # noqa:E501
            alt[(complex(side, c), (1+0j))] = (complex(1, 3*side+1-c), (-1+0j))  # noqa:E501
            # map 1<->3
            alt[(complex(c, 2*side), 0-1j)] = (complex(side+1, side+c), -1+0j)  # noqa:E501
            alt[(complex(side, side+c), -1+0j)] = (complex(c, 2*side+1), 0-1j)  # noqa:E501
            # map 1<->6
            alt[(complex(c, 3*side+1), 0+1j)] = (complex(3*side+1-c, 4*side), 0-1j)  # noqa:E501
            alt[(complex(2*side, 3*side+c), 0+1j)] = (complex(3*side, side+1-c), 0-1j)  # noqa:E501
            # map 2<->6
            alt[(complex(side+c, 0), 0-1j)] = (complex(3*side, 4*side+1-c), 1+0j)  # noqa:E501
            alt[(complex(3*side+1, 3*side+c), 0+1j)] = (complex(2*side+1-c, 1), -1+0j)  # noqa:E501
            # map 2<->5
            alt[(complex(2*side+1, c), -1+0j)] = (complex(3*side, 3*side+1-c), 1+0j)  # noqa:E501
            alt[(complex(3*side+1, 2*side+c), 1+0j)] = (complex(2*side, side+1-c), -1+0j)  # noqa:E501
            # map 3<->5
            alt[(complex(2*side+1, side+c), -1+0j)] = (complex(3*side+1-c, 2*side+1), 0+1j)  # noqa:E501
            alt[(complex(2*side+c, 2*side), 0-1j)] = (complex(2*side, 2*side+1-c), 1+0j)  # noqa:E501
            # map 4<->6
            alt[(complex(side+c, 3*side+1), 0+1j)] = (complex(2*side+1, 4*side+1-c), 1+0j)  # noqa:E501
            alt[(complex(2*side, 3*side+c), -1+0j)] = (complex(2*side+1-c, 3*side), 0-1j)  # noqa:E501
    else:
        side = max(p.real for p in board) // 4
        for c in range(1, int(side)+1):
            """
               111222
               111222
               111222
               333
               333
               333
            444555
            444555
            444555
            666
            666
            666
            """
            # map 1<->6
            alt[(complex(0, side+c), -1+0j)] = (complex(3*side+c, 1), 0+1j)  # noqa:E501
            alt[(complex(3*side+c, 0), 0-1j)] = (complex(1, side+c), -1+0j)  # noqa:E501
            # map 1<->4
            alt[(complex(c, side), 0-1j)] = (complex(3*side+1-c, 1), 0+1j)  # noqa:E501
            alt[(complex(2*side+c, 0), 0-1j)] = (complex(side+1-c, side+1), 0+1j)  # noqa:E501
            # map 2<->6
            alt[(complex(0, 2*side+c), -1+0j)] = (complex(4*side, c), -1+0j)  # noqa:E501
            alt[(complex(4*side+1, c), 1+0j)] = (complex(1, 2*side+c), 1+0j)  # noqa:E501
            # map 2<->5
            alt[(complex(c, 3*side+1), 0+1j)] = (complex(3*side+1-c, 2*side), 0-1j)  # noqa:E501
            alt[(complex(2*side+c, 2*side+1), 0+1j)] = (complex(3*side, side+1-c), 0-1j)  # noqa:E501
            # map 2<->3
            alt[(complex(side+1, 2*side+c), 1+0j)] = (complex(side+c, 2*side), 0-1j)  # noqa:E501
            alt[(complex(side+c, 2*side+1), 0+1j)] = (complex(side, 2*side+c), -1+0j)  # noqa:E501
            # map 3<->4
            alt[(complex(side+c, side), 0-1j)] = (complex(2*side+1, c), 1+0j)  # noqa:E501
            alt[(complex(2*side, c), -1+0j)] = (complex(side+c, side+1), 0+1j)  # noqa:E501
            # map 5<->6
            alt[(complex(3*side+1, side+c), 1+0j)] = (complex(3*side+c, side), 0-1j)  # noqa:E501
            alt[(complex(3*side+c, side+1), 0+1j)] = (complex(3*side, side+c), -1+0j)  # noqa:E501
    pos = 1+1j
    heading = 0+1j
    while board.get(pos) != '.':
        pos += heading
    for d, direction in enumerate(directions):
        if direction == 'L':
            # 0+1j -> -1+0j -> 0-1j -> 1+0j
            heading = complex(-heading.imag, heading.real)
            continue
        elif direction == 'R':
            # 0+1j -> 1+0j -> 0-1j -> 1+0j
            heading = complex(heading.imag, -heading.real)
            continue
        assert isinstance(direction, int)
        for _ in range(direction):
            step = pos + heading
            step_heading = heading
            if board.get(step) is None:
                assert (step, step_heading) in alt
                (step, step_heading) = alt[(step, step_heading)]
            if board[step] == '#':
                break
            assert board[step] == '.'
            pos, heading = step, step_heading
    headings = (0+1j, 1+0j, 0-1j, -1+0j)
    return int(1000 * int(pos.real) + 4 * int(pos.imag) + headings.index(heading))  # noqa:E501


def parse(text):
    mapping, code = text.rstrip().split('\n\n')
    directions = []
    for direction in re.findall(r'(\d+|R|L)', code):
        if direction.isdigit():
            direction = int(direction)
        directions.append(direction)
    points = {}
    for r, row in enumerate(mapping.split('\n'), 1):
        for c, char in enumerate(row, 1):
            if char == ' ':
                continue
            assert char in ('#', '.')
            points[complex(r, c)] = char
    return points, directions


TEST = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


if __name__ == "__main__":
    assert part1(parse(TEST.strip('\n'))) == 6032
    assert part2(parse(TEST.strip('\n')), test=True) == 5031
    LINES = parse(get_input(day=22, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
