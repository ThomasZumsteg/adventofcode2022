use common::get_input;

type Input = Vec<(usize, usize)>;

fn part1(hands: &Input) -> usize {
    hands.iter().map(|&(elf, me)| {
        (1 + me) + if me == ((elf + 1) % 3) { 6 }
        else if ((me + 1) % 3) == elf { 0 }
        else if me == elf { 3 }
        else { unimplemented!() }
    }).sum()
}

fn part2(hands: &Input) -> usize {
    hands.iter().map(|&(elf, me)| {
        match me {
            0 => 1 + ((elf + 2) % 3),
            1 => 4 + elf,
            2 => 7 + ((elf + 1) % 3),
            _ => unimplemented!()
        }
    }).sum()
}

fn parse(text: String) -> Input {
    text.trim().split("\n").map(|line| {
        let chars: Vec<char> = line.chars().collect();
        let index = |chars: &str, c: char| chars.chars().position(|p| p == c).unwrap();
        assert!(chars.len() == 3 && chars[1] == ' ');
        (index("ABC", chars[0]), index("XYZ", chars[2]))
    }).collect()
}

fn main() {
    let input = parse(get_input(02, 2022));
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
