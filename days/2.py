TEST_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
TEST_RESULT_1 = 1227775554
TEST_RESULT_2 = 4174379265

def chunks(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def part1(input):
    ranges = [
        tuple(x.split('-'))
        for x in input.replace("\n","").split(",")
    ]
    total = 0
    for id_range in ranges:
        for id in range(int(id_range[0]), int(id_range[1])+1):
            # split the id in half, see if they match
            sid = str(id)
            if len(sid) % 2 != 0:
                # if the length of the string is odd then it can't be made of a sequence repeated twice
                continue
            h1 = sid[0:int(len(sid)/2)]
            h2 = sid[int(len(sid)/2):]
            if h1 == h2:
                total += id
    return total

def part2(input):
    ranges = [
        tuple(x.split('-'))
        for x in input.replace("\n","").split(",")
    ]
    total = 0
    for id_range in ranges:
        for id in range(int(id_range[0]), int(id_range[1])+1):
            sid = str(id)
            # check whether the ID is made of a repeated sequence
            # - get the length of the ID
            lsid = len(sid)
            #   - find the factors of the ID
            #     - loop 1 - (ID / 2)
            for i in range(1, int(lsid / 2) + 1):
            #     - if i % ID == 0 then divide the ID into sections that many characters long
                if lsid % i == 0:
            #     - compare sections and see if they are all equal
                    sections = chunks(sid, i)
                    match = all(seg == sections[0] for seg in sections)
                    if match:
                        # print(f"{sid} is made up of repeating {sections[0]}s")
                        total += id
                        break
    return total
