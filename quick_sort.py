#QuickSort:

A = [12, 45, 10, 11, 7, 100, 65, 3,  12, 44]

def quickSort(input):
    left = []
    right = []
    equal = []

    if len(input) > 0:
        pivot = input[0]

        for i in input:
            if i > pivot:
                right.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                left.append(i)

        return quickSort(left) + equal + quickSort(right)
    else:
        return input
print A
b = quickSort(A)
print b

