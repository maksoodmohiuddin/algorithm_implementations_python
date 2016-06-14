import random

def answer(x):
    num_train_cars = len(x)
    # find mean
    mean = sum(x) / num_train_cars

    # last car gets 'uneven' numbers
    for train_car in range(num_train_cars - 1):
        rabbits_in_train_car = mean - x[train_car]

        # if car has too many or too few adjust with next car
        x[train_car] += rabbits_in_train_car
        x[train_car+1] -= rabbits_in_train_car
        rabbits_in_train_car -= rabbits_in_train_car

    return sum(z == mean for z in x)

test = [0, 1000000]
print answer(test)

test1 = [1, 4, 1]
print answer(test1)
#3

test2 = [1, 2]
print answer(test2)
# 1

test3 = [1, 4, 1, 3, 1, 10000, 0, 56, 88, 324, 435345, 1333, 43543, 23424]
print answer(test3)

test4 = random.sample(range(0, 1000000), 100)
print answer(test4)