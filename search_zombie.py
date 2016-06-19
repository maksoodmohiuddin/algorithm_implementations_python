import random

def answer(food, grid):
    # solved using a variation of A star search algorithm but instead taking highest path cost
    n = len(grid)
    row = 0
    column = 0
    start_node = (row, column)
    # tuple: pathcost, list of nodes
    node = [0, [start_node]]
    frontier = []
    frontier.append(node)
    goal_node = (n-1, n-1)

    while frontier:
        frontier.sort(key=lambda x: x[0])
        node = frontier.pop(len(frontier) - 1)
        pathcost = node[0]
        path = node[1]
        row, column = path[len(path) - 1]

        # check if a path is found
        if row == goal_node[0] and column == goal_node[1]:
            escape_path = node[1]
            #print escape_path
            path_cost = 0
            for path in escape_path:
                row, column = path
                node_cost = grid[row][column]
                path_cost += node_cost
            return food - path_cost

        child_nodes = []
        if column + 1 < n:
            right_child = row, column + 1
            child_nodes.append(right_child)

        if row + 1 < n:
            down_child = row + 1, column
            child_nodes.append(down_child)

        for child in child_nodes:
            newpath = list(path)
            newpath.append(child)

            child_row, child_column = child
            cost = grid[child_row][child_column]
            newpathcost = pathcost + cost
            new_node = [newpathcost, newpath]
            if newpathcost <= food:
                frontier.append(new_node)

    return -1

food1 = 7
grid1 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
print answer(food1, grid1)
# 0

food2 = 12
grid2 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
print answer(food2, grid2)
# 1

food3 = 12
grid3 = [[0, 2, 5], [1, 1, 5], [2, 1, 1]]
print answer(food3, grid3)
# 3

food4 = 7
grid4 = [[0, 2, 1], [1, 4, 5], [2, 1, 1]]
print answer(food4, grid4)
# 0

food5 = 8
grid5 = [[0, 1, 1], [5, 1, 1], [2, 2, 2]]
print answer(food5, grid5)
# 2,

food6 = 8
grid6 = [[0, 1, 1], [5, 5, 5], [2, 2, 2]]
print answer(food6, grid6)
# -1

food7 = 201
grid7 = [[0, 200], [1, 200]]
print answer(food7, grid7)
# 0

food8 = 101
grid8 = [[0, 1, 2, 4, 5, 6, 7, 9, 1, 4]]
for i in range(9):
    test = random.sample(range(0, 10), 10)
    grid8.append(test)
#print answer(food8, grid8)

food9 = 101
grid9 = [[0, 1, 2, 4, 5, 6, 7, 9, 1, 4], [2, 7, 0, 3, 8, 9, 5, 1, 6, 4], [0, 1, 8, 4, 3, 6, 5, 2, 9, 7], [4, 3, 2, 7, 5, 1, 0, 9, 6, 8], [4, 8, 0, 2, 3, 1, 6, 5, 7, 9], [5, 3, 9, 8, 2, 4, 0, 7, 6, 1], [9, 2, 5, 6, 3, 0, 7, 4, 8, 1], [8, 2, 4, 1, 5, 6, 3, 0, 9, 7], [6, 0, 8, 5, 1, 2, 4, 3, 7, 9], [3, 7, 8, 2, 9, 0, 1, 4, 6, 5]]
print answer(food9, grid9)