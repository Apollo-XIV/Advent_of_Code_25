import argparse
import importlib
import utils

parser = argparse.ArgumentParser(
    prog = "aoc25"
)
parser.add_argument("day")
parser.add_argument("--part", required = False, type = int)
args = parser.parse_args()
day = importlib.import_module(args.day)
input = utils.get_day_input(args.day)
match args.part:
    case 1:
        output = day.part1(input)
        print(output)
    case 2:
        output = day.part2(input)
        print(output)
    case _:
        output = day.part1(input)
        print(output)
        output = day.part2(input)
        print(output)
