import argparse
import importlib
import utils

parser = argparse.ArgumentParser(
    prog = "aoc25"
)
parser.add_argument("day")
parser.add_argument("--part", required = False, type = int)
parser.add_argument("--test", action = "store_true")
args = parser.parse_args()
day = importlib.import_module(args.day)
if args.test:
    input = day.TEST_INPUT
else:
    input = utils.get_day_input(args.day)
output = None
match args.part:
    case 1:
        output = day.part1(input)
    case 2:
        output = day.part2(input)
    # case _:
    #     output = day.part1(input)
    #     output = day.part2(input)
print(output)
if args.test and args.part == 1:
    if day.TEST_RESULT_1 == output:
        print("CORRECT")
    else:
        print(f"INCORRECT: output should be {day.TEST_RESULT_1}")
if args.test and args.part == 2:
    if day.TEST_RESULT_2 == output:
        print("CORRECT")
    else:
        print(f"INCORRECT: output should be {day.TEST_RESULT_2}")
