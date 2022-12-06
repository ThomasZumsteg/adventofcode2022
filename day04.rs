use common::get_input;

type Input = Vec<((usize, usize), (usize, usize))>;

fn part1(ranges: &Input) -> usize {
    ranges.iter().filter(|(first, second)|
        (second.0 <= first.0 && first.1 <= second.1) ||
        (first.0 <= second.0 && second.1 <= first.1)
    ).count()
}


fn part2(ranges: &Input) -> usize {
    ranges.iter().filter(|(first, second)| !(first.1 < second.0 || second.1 < first.0)).count()
}

fn parse(text: String) -> Input {
    text.trim().split("\n").map(|line| {
        let parts = line.split(",")
            .map(|p| p.split("-").map(|n| n.parse::<usize>().unwrap())).flatten()
            .collect::<Vec<usize>>();
        assert!(parts.len() == 4);
        ((parts[0], parts[1]), (parts[2], parts[3]))
    }).collect()
}

fn main() {
    let input = parse(get_input(04, 2022));
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
