"""Solution to day 7 for Advent of Code"""

from get_input import get_input


def get_sizes(commands):
    dirs = {}
    files = {}
    cwd = []
    for cmd, output in commands:
        if cmd[0] == "cd":
            if cmd[1] == "..":
                cwd.pop()
            else:
                cwd.append(cmd[1])
        else:
            assert cmd[0] == "ls"
            subdirs = []
            for size, name in output:
                cwd.append(name)
                subdirs.append(tuple(cwd))
                if size != "dir":
                    files[tuple(cwd)] = int(size)
                cwd.pop()
            dirs[tuple(cwd)] = subdirs
    queue = [("/",)]
    sizes = files.copy()
    while queue != []:
        dr = queue.pop(0)
        if dr in sizes:
            continue
        try:
            size = sum(sizes[subdir] for subdir in dirs[dr])
        except KeyError:
            queue.extend(dirs[dr])
            queue.append(dr)
        else:
            sizes[dr] = size
    return {k: v for k, v in sizes.items() if k not in files}


def part1(commands):
    sizes = get_sizes(commands)
    return sum(size for name, size in sizes.items() if size <= 100_000)


def part2(commands):
    sizes = get_sizes(commands)
    required = 30000000 - (70000000 - sizes[('/',)])
    assert required > 0
    possible = sorted((v, k) for k, v in sizes.items() if v > required)
    return possible[0][0]


def parse(text):
    commands = []
    for line in iter(text.strip().split("\n")):
        if line[0] == "$":
            output = []
            commands.append((tuple(line.split(' ')[1:]), output))
        else:
            output.append(tuple(line.split(' ')))
    return commands


TEST = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


if __name__ == "__main__":
    assert part1(parse(TEST)) == 95437
    assert part2(parse(TEST)) == 24933642
    LINES = parse(get_input(day=7, year=2022))
    print(f"Part 1: {part1(LINES)}")
    print(f"Part 2: {part2(LINES)}")
