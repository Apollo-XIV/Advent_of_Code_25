TEST_INPUT =  """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
TEST_RESULT_1 = 3
TEST_RESULT_2 = 14

def part1(input):
    ranges, *ids = input.split("\n\n")
    ranges = [
        range(low, high + 1)
        for low, high in [
            tuple(map(int, pair.split("-")))
            for pair in ranges.splitlines()
        ]
    ]

    counter = 0
    for sid in ids[0].strip().splitlines():
        id = int(sid)
        for valid_range in ranges:
            print(id, "in", valid_range, "\t:", id in valid_range)
            if id in valid_range:
                counter += 1
                break
    return counter

def merge_ranges(ranges):
    # convert to inclusive bounds for easier maths
    intervals = [(r.start, r.stop - 1) for r in ranges]
    intervals.sort()

    merged = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= cur_end + 1:  # overlap or adjacency
            cur_end = max(cur_end, end)
        else:
            merged.append(range(cur_start, cur_end + 1))
            cur_start, cur_end = start, end

    merged.append(range(cur_start, cur_end + 1))
    return merged

def part2(input):
    ranges, *ids = input.split("\n\n")
    ranges = [
        range(low, high + 1)
        for low, high in [
            tuple(map(int, pair.split("-")))
            for pair in ranges.splitlines()
        ]
    ]

    simplified_ranges = merge_ranges(ranges)

    total = sum(len(r) for r in simplified_ranges)
    return total
