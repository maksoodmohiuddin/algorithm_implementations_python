# 1, 2, 3, 4, 5, 6, 7
# 1, 1, 2, 3, 5, 8, 13
def fibo(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        p = 1
        c = 1
        i = 2
        while n > i:
            i += 1
            f = p + c
            p = c
            c = f
        return f


print fibo(7)