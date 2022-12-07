use common::get_input;
use std::collections::HashSet;

type Input = String;

fn find_start(buffer: &String, bufsize: usize) -> usize {
    let mut buf = Vec::new();
    for (i, item) in buffer.chars().enumerate() {
        buf.push(item);
        if buf.len() < bufsize { continue; }
        else if buf.len() > bufsize { buf.remove(0); }
        if buf.iter().collect::<HashSet<&char>>().len() == bufsize { return i + 1 }
    }
    unimplemented!()
}

fn part1(buffer: &Input) -> usize {
    find_start(buffer, 4)
}

fn part2(buffer: &Input) -> usize {
    find_start(buffer, 14)
}

fn main() {
    let input = get_input(06, 2022);
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
