from collections import defaultdict
TEST_INPUT =  """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
TEST_RESULT_1 = 21
TEST_RESULT_2 = 40

def trace_timelines(raw):
    lines = raw.splitlines()
    max_lines = len(lines)
    beams = defaultdict(int)
    beams[lines[0].index("S")] = 1 # beam index x timelines
    splits = 0
    for i, line in enumerate(lines):
        print(f"calculating {i}/{max_lines} ({(i/max_lines)*100}%): {sum(beams.values())} timelines")
        next_beams = defaultdict(int)
        # go through the beam indexes, see if there is a splitter
        for index, current_count in beams.items():
            # print(index, current_count, next_beams)
            if line[index] == "^":
                # if there is, add two beam indexes above and below the current index
                next_beams[index-1] += current_count
                next_beams[index+1] += current_count
                splits += 1
            else:
                # if not, leave the beam as is, adding it to the next row
                next_beams[index] += current_count
        beams = next_beams

    return splits, sum(beams.values())

def part1(raw):
    splits, _ = trace_timelines(raw)
    return splits

def part2(raw):
    _, timeline_count = trace_timelines(raw)
    return timeline_count
