#It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held,
#but a sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches
#you've built to house the fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be
#rescued from Professor Boolean's lab, you must compute how much standing water has accumulated on the rabbit hutches.

#Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top
# (and allowed to run off the sides). We'll assume all the hutches are square, have side length 1,
# and for the purposes of this problem we'll pretend that the hutch arrangement is two-dimensional.
# For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):

# ...X...
# .X.X...
# .X.X..X
# .XXX.XX
# XXXXXXX
# 1425123

# When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

#...X...
#.XOX...
#.XOXOOX
#.XXXOXX
#XXXXXXX
#1425123

# The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

# Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as a list,
# computes the total area of standing water accumulated when water is poured from the top and allowed to run off the sides.

# The heights array will have at least 1 element and at most 9000 elements.
# Each element will have a value of at least 1, and at most 100000.

import copy
from operator import sub
from itertools import imap
def answer(heights):
    original_heights = copy.deepcopy(heights)
    heights_length = len(heights)

    #print original_heights

    # flll: right to left
    for i in range(heights_length - 2, 0, -1):
        current = heights[i]
        right = heights[i+1]
        if right >= current:
            heights[i] = right
    #print heights

    # runoff: left to right
    for i in range(1, heights_length - 1, 1):
        current = heights[i]
        left = heights[i-1]
        if current >= left:
            if original_heights[i] >= left:
                # reset to original height
                heights[i] = original_heights[i]
            else:
                heights[i] = left
    #print heights

    numO = list(imap(sub, heights, original_heights))

    #print numO
    return sum(numO)

test1 = [1, 4, 2, 5, 1, 2, 3]
print answer(test1)
# 5

test2 = [1, 2, 3, 2, 1]
print answer(test2)
# 0

import  random
test3 = []
for i in range(9000):
    hutches = random.sample(range(0, 100000), 1)
    test3.append(hutches[0])
print test3

import time
start = time.time()
print answer(test3)
end = time.time()
print(end - start)

