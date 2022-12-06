use common::get_input;
use regex::Regex;

struct Instruction {
    from: usize,
    to: usize,
    boxes: usize,
}

impl Instruction {
    fn from_str(text: &str) -> Instruction {
        let re = Regex::new(r"move (\d+) from (\d+) to (\d+)").unwrap();
        let groups = re.captures(text).unwrap();
        let get_int = |n| groups.get(n).unwrap().as_str().parse::<usize>().unwrap();
        Instruction {
            boxes: get_int(1),
            from: get_int(2),
            to: get_int(3),
        }
    }
}


struct Input {
    boxes: Vec<Vec<char>>,
    instructions: Vec<Instruction>
}

impl Input {
    fn from_str(crates: Vec<&str>, instructions: Vec<&str>) -> Input {
        let crate_names = crates.last().unwrap().trim().split("   ")
            .map(|n| n.trim().parse::<usize>().unwrap()).collect::<Vec<usize>>();
        let mut boxes = vec![vec![]; crate_names.len()];
        for line in crates.iter().take(crates.len()-1) {
            let line = line.chars().enumerate().filter(|(n, _)| (n + 3) % 4 == 0);
            for (n, (_, chr)) in line.enumerate() {
                if chr != ' ' { boxes[n].insert(0, chr) }
            }
        }
        Input {
            boxes,
            instructions: instructions.iter().map(|i| Instruction::from_str(i)).collect()
        }
    }
}

fn part1(input: &Input) -> String {
    let mut crates = input.boxes.clone();
    for instruction in &input.instructions {
        for _ in 0..instruction.boxes {
            let crt = crates[instruction.from-1].pop().unwrap();
            crates[instruction.to-1].push(crt)
        }
    }
    crates.iter().map(|c| c.last().unwrap()).collect::<String>()
}

fn part2(input: &Input) -> String {
    let mut crates = input.boxes.clone();
    for instruction in &input.instructions {
        let len = crates[instruction.from-1].len();
        let mut crts = crates[instruction.from-1].drain((len-instruction.boxes)..len).collect::<Vec<char>>();
        crates[instruction.to-1].append(&mut crts)
    }
    crates.iter().map(|c| c.last().unwrap()).collect::<String>()
}

fn parse(text: String) -> Input {
    let mut lines = text.trim().split("\n").into_iter();
    let crates = lines.by_ref().take_while(|&l| l != "").collect();
    let instructions: Vec<&str> = lines.collect();
    Input::from_str(crates, instructions)
}

fn main() {
    let input = parse(get_input(05, 2022));
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
