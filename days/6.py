from functools import reduce
import operator as op

TEST_INPUT =  """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
TEST_RESULT_1 = 4277556
TEST_RESULT_2 = 3263827

def part1(input):
    *operands_list, operators = input.splitlines()
    operands_list = zip(*[map(int,line.split()) for line in operands_list])
    total = 0
    for operands, operator in zip(operands_list, operators.split()):
        match operator:
            case "*":
                total += reduce(op.mul, operands)
            case "+":
                total += reduce(op.add, operands)
    return total

def part2(input):
    *operands_list, operators_string = input.splitlines()
    # make it easier to find operators
    indexing_string = operators_string.replace("+", ".").replace("*", ".")
    total = 0
    while len(indexing_string) > 0:
        # use the operators to find each set of operands
        breakpoint = indexing_string.find(".", 1)
        if breakpoint == -1:
            breakpoint = len(indexing_string)+1
        # consume values from each line
        indexing_string = indexing_string[breakpoint:]
        operands = [line[0:breakpoint - 1] for line in operands_list]
        # operands are read vertically rather than horizontally
        operands = [int(''.join(chars)) for chars in zip(*operands)]
        operands_list = [line[breakpoint:] for line in operands_list]
        # the operator is easy to consume
        operator = operators_string[0]
        operators_string = operators_string[breakpoint:]
        # compute the calculation and add it to the total
        match operator:
            case "*":
                total += reduce(op.mul, operands)
            case "+":
                total += reduce(op.add, operands)
        
    return total
