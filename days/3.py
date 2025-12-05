TEST_INPUT =  """987654321111111
811111111111119
234234234234278
818181911112111"""
TEST_RESULT_1 = 357
TEST_RESULT_2 = 3121910778619

def part1(input):
    banks = [x for x in input.split("\n") if x != ""]
    total = 0
    for bank in banks:
        # search all but the last digit and find the largest one (a two digit number will always be bigger than a one digit one)
        max = (0,0)
        for i in range(len(bank) - 1):
            cmp = int(bank[i])
            if cmp > max[0]:
                max = (cmp, i)
        # find the largest number after the previous max
        start = max[1]+1
        max2 = (int(bank[start]), start)
        for i in range(start, len(bank)):
            cmp = int(bank[i])
            if cmp > max2[0]:
                max2 = (cmp, i)
        total += int(f"{max[0]}{max2[0]}")
    return total
            
def part2(input):
    banks = [x for x in input.split("\n") if x != ""]
    total = 0
    for bank in banks:
        def find_largest_before(start, characters_after):
            # find the first largest digit that has enough characters after it to complete the set
            # for example, on the first comparisson we need at least 11 characters left
            max = (0,0)
            for i in range(start, len(bank) - characters_after):
                cmp = int(bank[i])
                if cmp > max[0]:
                    max = (cmp, i)
            return max

        best = []
        start = 0
        for i in range(11,-1,-1):
            next_best = find_largest_before(start, i)
            start = next_best[1] + 1
            best.append(next_best)
        best = int("".join([str(x[0]) for x in best]))
        total += best
    return total

    
