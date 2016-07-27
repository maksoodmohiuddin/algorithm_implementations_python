# Determine if any 3 integers in an array sum to 0.
# https://en.wikipedia.org/wiki/3SUM

def threeSum(nums):
    triplets = {}
    result = []
    l = len(nums)
    for i in range(l):
        k = i
        for j in range(k,l - 2):
            triplet = nums[i], nums[j+1], nums[j+2]

            if triplet not in triplets:
                triplets[triplet] = triplet
                if sum(list(triplet)) == 0:
                    result.append(list(triplet))

    return result


# test
print threeSum([-1, 0, 1, 2, -1, -4])
print threeSum([0, 0, 0, 0])
print threeSum([-1, 0, 1, 0])


#A solution set is:
#[
#  [-1, 0, 1],

#  [-1, -1, 2]
#]
