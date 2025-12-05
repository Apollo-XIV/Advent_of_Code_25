from enum import Enum
from itertools import product

TEST_INPUT =  """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
TEST_RESULT_1 = 13
TEST_RESULT_2 = 43

class State(Enum):
    NOTHING = "."
    PAPER = "@"
    REMOVABLE_PAPER = "x"

    def __repr__(self):
        return self.value

    def from_char(char: str):
        match char:
            case ".":
                return State.NOTHING
            case "@":
                return State.PAPER

def find_accessible_spaces(grid):
    next_grid = [[State.NOTHING for _ in range(len(row))] for row in grid]
    kernel = [x for x in list(product(range(-1, 2), repeat=2)) if x != (0,0)]
    # loop over every space in the grid
    accessible_spaces = 0
    for y, row in enumerate(grid):
        for x, space in enumerate(row):
            # search the nearby squares and tally
            if space != State.PAPER:
                continue
            filled_spaces = 0
            for dy, dx in kernel:
                ny, nx = y + dy, x + dx

                if not (0 <= ny < len(grid) and 0 <= nx < len(row)):
                    continue

                if grid[ny][nx] is State.PAPER:
                    filled_spaces += 1

            if filled_spaces < 4:
                accessible_spaces += 1
                next_grid[y][x] = State.REMOVABLE_PAPER
            else:
                next_grid[y][x] = space
                
    [print("".join([space.value for space in row])) for row in next_grid]
    return accessible_spaces, next_grid

def part1(input):
    grid = [[State.from_char(x) for x in y] for y in input.strip().split("\n")]
    accessible_spaces, _ = find_accessible_spaces(grid)
    return accessible_spaces

def part2(input):
    grid = [[State.from_char(x) for x in y] for y in input.strip().split("\n")]
    total = 0
    out = 1
    while out > 0:
        out, grid = find_accessible_spaces(grid)
        total += out
    return total
