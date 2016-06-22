# 1, 2, 3, 4, 5, 6, 7
# 1, 1, 2, 3, 5, 8, 13
# Write a program which stores the results of the numbers in a Fibonancci sequence in an array
def fibo_iteraritve(n):
    fibo_sequence = [0]
    if n <= 1:
        return fibo_sequence

    prev = 0
    prev_prev = 1
    for i in range(1, n):
        fibo = prev + prev_prev
        fibo_sequence.append(prev + prev_prev)
        prev_prev = prev
        prev = fibo

    return fibo_sequence

print fibo_iteraritve(8)



def fibo_recursive(n):
    if n <= 2:
        return 1

    return fibo_recursive(n-2) + fibo_recursive(n-1)

print fibo_recursive(8)