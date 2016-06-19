def get_frontier_node(frontier):
    node_costs = []
    for node in frontier:
        node_costs.append(node[0])
    maxval = max(node_costs)
    indices = [index for index, val in enumerate(node_costs) if val == maxval]
    first = True
    remove_count = 1
    for i in indices:
        # grab first
        if first:
            node = frontier.pop(i)
            first = False
        else:
            frontier.pop(i - remove_count)
            remove_count += 1
    return node

def answer(food, grid):
    # solved using a variation of dijkstra's algorithm but instead taking highest path cost
    # Also borrowed a trick from A star search
    n = len(grid)
    row = 0
    column = 0
    pos = (row, column)
    # tuple: heuristiccost, totalpathcost, list of nodes
    node = 0, 0, [pos]
    frontier = []
    frontier.append(node)
    goalpos = (n-1, n-1)

    while frontier:
        node = get_frontier_node(frontier)
        pathcost = node[1]
        path = node[2]
        row, column = path[len(path) - 1]

        # check if a path is found
        if row == goalpos[0] and column == goalpos[1]:
            escape_path = node[2]
            print escape_path
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
            cost =  grid[child_row][child_column]
            newpathcost = pathcost + cost
            heuristic = (n - child_row - 1) * 10 + (n - child_column - 1) * 10
            heuristiccost = newpathcost + heuristic

            test = frontier

            node = heuristiccost, newpathcost, newpath
            if newpathcost <= food:
                frontier.append(node)
    return -1


def answer1(food, grid):
    # solved using a variation of dijkstra's algorithm but instead taking highest path cost
    # Also borrowed a trick from A star search
    n = len(grid)

    # initialization
    zombie_sucks = True
    current_column = 0
    current_row = 0
    path_cost_so_far = 0
    heuristic_cost = (n * 2) - 2

    while zombie_sucks:

        if current_column + 1 < n:
            right_room_cost = grid[current_row][current_column + 1]

            # if last colmun, calculate actual cost since we only can go below
            if current_column + 1 == (n-1):
                below_actual_path_cost = 0
                for index in range(current_row, n):
                    below_actual_path_cost += grid[index][current_column + 1]

                # its a feasible path
                if below_actual_path_cost <= food:
                    right_path_cost = path_cost_so_far + below_actual_path_cost
                else:
                    right_path_cost = 0
            else:
                right_path_cost = path_cost_so_far + right_room_cost + heuristic_cost - 1
                if heuristic_cost > food:
                    right_path_cost = 0

        else:
            right_path_cost = 0

        if current_row + 1 < n:
            below_room_cost = grid[current_row + 1][current_column]

            # if last row, calculate actual cost since we only can go right
            if current_row + 1 == (n-1):
                right_actual_path_cost = 0
                for index in range(current_column, n):
                    right_actual_path_cost += grid[current_row + 1][index]

                # its a feasible path
                if right_actual_path_cost <= food:
                    below_path_cost = path_cost_so_far + right_actual_path_cost
                else:
                    below_path_cost = 0
            else:
                below_path_cost = path_cost_so_far + below_room_cost + heuristic_cost - 1
                if below_path_cost > food:
                    below_path_cost = 0
        else:
            below_path_cost = 0

        if right_path_cost > below_path_cost:
            current_column += 1
            path_cost_so_far += right_room_cost
            food -= right_room_cost
        elif right_path_cost < below_path_cost:
            current_row += 1
            path_cost_so_far += below_room_cost
            food -= below_room_cost
        elif current_row == (n-1) and current_column < (n-1):
            current_column += 1
            path_cost_so_far += right_room_cost
            food -= right_room_cost
        elif current_column == (n-1) and current_row < (n-1):
            current_row += 1
            path_cost_so_far += below_room_cost
            food -= below_room_cost
        else:
            return -1

        heuristic_cost -= 1

        if (current_column == (n-1) and current_row == (n-1)) or food < 0:
            zombie_sucks = False

    return food


def answer2(food, grid):
    # solved using a variation of dijkstra's algorithm but instead taking highest path cost
    # Also borrowed a trick from A star search

    # initialization
    n = len(grid)
    zombie_sucks = True
    column = 0
    row = 0
    explored = []

    while zombie_sucks:
        pos_right = row, column + 1
        if pos_right not in explored and column + 1 < n:
            right_room_cost = grid[row][column + 1]
        else:
            right_room_cost = 0

        pos_below = row + 1, column
        if pos_below not in explored and row + 1 < n:
            below_room_cost = grid[row + 1][column]
        else:
            below_room_cost = 0

        if right_room_cost > below_room_cost:
            column += 1
            if right_room_cost < food:
                food -= right_room_cost
            else:
                pos = row, column
                explored.append(pos)
        elif right_room_cost < below_room_cost:
            row += 1
            if below_room_cost < food:
                food -= below_room_cost
            else:
                pos = row, column
                explored.append(pos)


food1 = 7
grid1 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
#print answer(food1, grid1)
# 0

food2 = 12
grid2 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
#print answer(food2, grid2)
# 1

food3 = 12
grid3 = [[0, 2, 5], [1, 1, 5], [2, 1, 1]]
#print answer(food3, grid3)
# 3

food4 = 7
grid4 = [[0, 2, 1], [1, 4, 5], [2, 1, 1]]
#print answer(food4, grid4)
# 0

food5 = 8
grid5 = [[0, 1, 1], [5, 1, 1], [2, 2, 2]]
print answer(food5, grid5)
# 2, failing

food6 = 8
grid6 = [[0, 1, 1], [5, 5, 5], [2, 2, 2]]
#print answer(food6, grid6)
# -1

food7 = 201
grid7 = [[0, 200], [1, 200]]
print answer(food7, grid7)
# 2, failing