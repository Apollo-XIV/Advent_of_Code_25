from itertools import combinations
import math
TEST_INPUT =  """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
TEST_RESULT_1 = 40
TEST_RESULT_2 = 25272

def distance_between(a, b, pairwise=False):
    powers = sum([math.pow(bx - ax, 2) for ax, bx in zip(a,b)])
    if pairwise:
        return powers
    return math.sqrt(powers)

def part1(raw):
    junction_boxes = [tuple(map(int,x.split(","))) for x in raw.splitlines()]
    desired_number_of_pairs = 1000 if len(junction_boxes) > 20 else 10
    pairs = []
    for i, j in combinations(range(len(junction_boxes)), 2):
        pairs.append((distance_between(junction_boxes[i], junction_boxes[j], pairwise = True), i, j))
    pairs.sort(key = lambda t: t[0])

    forest = DSU(len(junction_boxes))
    count = 0
    for dist, a, b in pairs:
        if forest.find(a) != forest.find(b): # make sure these boxes aren't already in the same circuit
            forest.union(a, b) # join them, because this is the next shortest link
        count += 1
        if count == desired_number_of_pairs: # stop making pairs after we've made the predecided amount
            break

    # now we just need to find the 3 largest numbers in the size list of the DSU
    roots = {forest.find(i) for i in range(len(junction_boxes))}
    sizes = [forest.size[i] for i in roots]
    sizes.sort()
    return math.prod(sizes[-3:])

def part2(raw):
    junction_boxes = [tuple(map(int,x.split(","))) for x in raw.splitlines()]
    pairs = []
    for i, j in combinations(range(len(junction_boxes)), 2):
        pairs.append((distance_between(junction_boxes[i], junction_boxes[j], pairwise = True), i, j))
    pairs.sort(key = lambda t: t[0])

    forest = DSU(len(junction_boxes))
    for dist, a, b in pairs:
        if forest.find(a) != forest.find(b): # make sure these boxes aren't already in the same circuit
            forest.union(a, b) # join them, because this is the next shortest link

        # do we have a single root yet? If so, we've got one giant circuit and we can get our result
        if forest.circuits == 1:
            # the puzzle wants the "distance from the wall of the first two boxes that are joined to complete the circuit"
            # this just means take the x coords of the two and multiply them. Multiplication is just used because the puzzle says so
            return junction_boxes[a][0] * junction_boxes[b][0]

class DSU:
    def __init__(self, n):
        self.parent = list(range(n)) # a list of pointers to each point,
        # currently each one lines up with its index in this list, however, as
        # we go we're gonna replace these indexes to point at the one it's
        # connected to. If you follow all the pointers, you'll eventually reach
        # a pointer that points to itself.
        self.size = [1] * n # This is a list of how big the circuit would be for each point, if that point was the root. This is because we stop updating the ranks of points that are no longer roots
        self.circuits = n

    def find(self, i):
        if self.parent[i] != i: # If a pointer doesn't point to itself, we need to find what it does point to
            self.parent[i] = self.find(self.parent[i]) # this is acually doing two things:
            # firstly, it's gonna recurse and keep finding the next pointer until we do get one that returns itself
            # secondly, we always find the fastest path to the pointer, as we save the one closest to the root for next time
            # thirdly, this means that it can still update as well, as we have to check the pointer each time
        return self.parent[i]

    def union(self, x, y):
        # find the root of each of these new points. This is how we know which circuit they belong to
        s1 = self.find(x)
        s2 = self.find(y)
        self.circuits -= 1

        if s1 == s2: # if both roots are the same, that means they're already in the same circuit. We can skip it.
            return

        if self.size[s1] < self.size[s2]:
            # if s1 is a smaller circuit than s2, lets point s1 at s2, effectively it into s2
            self.parent[s1] = s2
            self.size[s2] += self.size[s1]
        elif self.size[s1] > self.size[s2]:
            # if s1 is actually the bigger circuit, we're gonna add s2 it instead
            self.parent[s2] = s1
            self.size[s1] += self.size[s2]
        else:
            # if both circuits are the same size, we add one to the other and
            self.parent[s2] = s1
            self.size[s1] *= 2 # double the size because we're adding it to itself

