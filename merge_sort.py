#MergeSort:

a= [14, 33, 27, 10, 35, 19, 42, 44]

def merge_sort(input):
    result = []
    input_len = len(input)
    if input_len == 1:
        return input

    middle = input_len / 2

    left_input = input[0:middle]
    right_input = input[middle:input_len]

    left = merge_sort(left_input)
    right = merge_sort(right_input)

    #print left
    #print right
    l = 0
    r = 0

    while (len(left) > l and len(right) > r):
        if(left[l] < right[r]):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    #result.append(left[l:])
    #result.append(right[r:])

    return result

print a
print merge_sort(a)

def mergesort_new(a):
    result = []

    if len(a) == 1:
        return a

    mid = len(a) / 2
    left_in = a[:mid]
    right_in = a[mid:]

    left =  mergesort_new(left_in)
    right = mergesort_new(right_in)

    i = 0
    j = 0

    while (len(left) > i and len(right) > j):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

b= [14, 33, 27, 9, 35, 19, 42, 44]
print mergesort_new(b)