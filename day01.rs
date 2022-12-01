use common::get_input;
use std::collections::BinaryHeap;

type Input = Vec<Vec<usize>>;

fn part1(elves: &Input) -> usize {
    elves.iter().map(|elf| elf.iter().sum()).max().unwrap()
}

fn part2(elves: &Input) -> usize {
    elves.iter()
        .map(|elf| elf.iter().sum())
        .collect::<BinaryHeap<usize>>().iter()
        .take(3).sum()
}

fn parse(text: String) -> Input {
    text.trim().split("\n\n").map(|group| {
        group.split("\n").map(|n| n.parse::<usize>().unwrap()).collect()
    }).collect()
}

fn main() {
    let input = parse(get_input(01, 2022));
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
