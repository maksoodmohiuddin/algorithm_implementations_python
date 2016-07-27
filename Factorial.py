def factorial(n):
   f = 1
   for i in range(n):
       f = f * (i + 1)
   return f

print factorial(5)

def factorial_rec(n):
    if n < 1:
        return 1
    else:
        result = n * factorial_rec(n-1)

    return result

print factorial_rec(5)

