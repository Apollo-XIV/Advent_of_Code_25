
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

