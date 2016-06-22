# 5. Given a list of integers and a target number, list all pairs that sum up to that number, 2 sum
def twoSum(nums, target):
    length = len(nums)

    for i in range(length):
       for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]


print twoSum([2, 7, 11, 15], 9)

def twoSumHash(nums, target):
    dict = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict:
            return [dict[complement], i]
        dict[nums[i]] = i

print twoSumHash([2, 7, 11, 15], 9)


def twoSum(N, x):
    dict = {}

    for i in range(len(N)):
        complement = x - N[i]
        if complement in dict:
            return True
        dict[N[i]] = i

    return False

print twoSum([2, 7, 11, 15], 9)
print twoSum([2, 7, 11, 15], 3)
#