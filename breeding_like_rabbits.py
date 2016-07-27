# Practice Recursive Algorithm with memoziation

# As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead of following the Fibonacci sequence
# like all good rabbits do, the zombit population changes according to this bizarre formula,
# where R(n) is the number of zombits at time n:

# R(0) = 1
# R(1) = 1
# R(2) = 2
# R(2n) = R(n) + R(n + 1) + n (for n > 1)
# R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

# (At time 2, we realized the difficulty of a breeding program with only one zombit and so added an additional zombit.)

# Being bored with the day-to-day duties of a henchman, a bunch of Professor Boolean's minions passed the time by playing
# a guessing game: when will the zombit population be equal to a certain amount? Then, some clever minion objected that
# this was too easy, and proposed a slightly different game: when is the last time that the zombit population will be
# equal to a certain amount? And thus, much fun was had, and much merry was made.

# (Not in this story: Professor Boolean later downsizes his operation, and you can guess what happens to these minions.)

# Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n
# such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None".
# S will be a positive integer no greater than 10^25.


def recursive_breeding(n):
    if n == 0:
        return 1

    if n == 1 or n == 2:
        return n

    if n % 2 == 0:
        n /= 2
        return recursive_breeding(n) + recursive_breeding(n + 1) + n
    else:
        n /= 2
        return recursive_breeding(n - 1) + recursive_breeding(n) + 1


def answer(strS):
    s = int(strS)

    # there's possibility of n > s
    if s < 10:
        for i in range(s):
            n = recursive_breeding(i)
            if n == s:
                return str(i)
    # it will be n < s so we can use divide & conquer
    else:
        h = s / 2
        for i in range(h, s, 1):
            n = recursive_breeding(i)
            if n == s:
                return str(i)




    return "None"

test1 = "7"
# "4"

test2= "100"
# "None"

test3= "10000"
# "None"

print answer(test1)
print answer(test2)
#print answer(test3)

for i in range(0, 1000):
   print str(i) + ":" + str(recursive_breeding(i))
