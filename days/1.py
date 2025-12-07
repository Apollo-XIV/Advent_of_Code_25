TEST_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
TEST_RESULT_1 = 3
TEST_RESULT_2 = 6

def part1(input):
    turns = [x for x in input.split("\n") if x != ""]
    pos = 50
    tally = 0
    for turn in turns:
        dir = 1 if turn[0] == "R" else -1
        pos += dir * int(turn[1:])
        pos %= 100
        if pos == 0:
            tally += 1
    return tally

def part2(input):
    turns = [x for x in input.split("\n") if x != ""]
    pos = 50
    tally = 0
    for turn in turns:
        dir = 1 if turn[0] == "R" else -1
        delta = int(turn[1:])
        for i in range(delta):
            pos += 1 * dir
            pos %= 100
            if pos == 0:
                tally += 1
    return tally

