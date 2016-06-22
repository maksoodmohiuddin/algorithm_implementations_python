# Problem: Given a sequence of nonnegative integers A and an integer T, return whether there is a *continuous sequence* of A that sums up to exactly T
#Example:
#[23, 5, 4, 7, 2, 11], 20. Return True because 7 + 2 + 11 = 20
#[1, 3, 5, 23, 2], 8. Return True because 3 + 5 = 8
# [1, 3, 5, 23, 2], 7 Return False because no sequence in this array adds up to 7

def continuous_sequence(A, T):
    length = len(A)

    for i in range(length):
        num = A[i]
        if num <= T:
            for j in range(i + 1, length):
                num += A[j]
                if num > T:
                    break
                elif num == T:
                    return True
                else:
                    continue

    return False

print continuous_sequence([23, 5, 4, 7, 2, 11], 20)
print continuous_sequence([23, 5, 4, 7, 2, 11], 12)
print continuous_sequence([1, 3, 5, 23, 2], 8)
print continuous_sequence([1, 3, 5, 23, 2], 7)

