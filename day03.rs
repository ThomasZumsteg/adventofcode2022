use common::get_input;
use std::collections::HashSet;

type Input = Vec<String>;

fn part1(sacks: &Input) -> usize {
    sacks.iter().map(|s| {
        let len = s.len();
        let mut chars = s.chars();
        let sack_a = chars.by_ref().take(len / 2).collect::<HashSet<char>>();
        let sack_b = chars.collect::<HashSet<char>>();
        let common = sack_a.intersection(&sack_b).collect::<Vec<&char>>();
        assert!(common.len() == 1);
        match common.last().unwrap() {
            &&c if 'a' <= c && c <= 'z' => (c as usize) - ('a' as usize) + 1,
            &&c if 'A' <= c && c <= 'Z' => (c as usize) - ('A' as usize) + 27,
            _ => unimplemented!()
        }
    }).sum()
}

fn part2(sacks: &Input) -> usize {
    let mut sacks_iter = sacks.into_iter().map(|s| s.chars().collect::<HashSet<char>>());
    let mut total = 0;
    while let Some(group) = sacks_iter.next() {
        let common: HashSet<char> = sacks_iter.by_ref().take(2)
            .fold(group, |acc: HashSet<char>, s: HashSet<char>| &acc & &s);
        assert!(common.len() == 1);
        total += match common.iter().next().unwrap() {
            &c if 'a' <= c && c <= 'z' => (c as usize) - ('a' as usize) + 1,
            &c if 'A' <= c && c <= 'Z' => (c as usize) - ('A' as usize) + 27,
            _ => unimplemented!()
        };
    };
    total
}

fn parse(text: String) -> Input {
    text.trim().split("\n").map(|s| s.to_string()).collect()
}

fn main() {
    let input = parse(get_input(03, 2022));
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
