def answer(food, grid):
    n = len(grid)

    # initialization
    heuristic_cost = (n * 2) - 2
    current_column = 0
    current_row = 0
    zombie_sucks = True
    path_cost_so_far = 0
    right_room_cost = 0
    below_room_cost = 0
    right_path_cost = 0
    below_path_cost = 0

    while zombie_sucks:

        if current_column + 1 < n:
            right_room_cost = grid[current_row][current_column + 1]

            # if last colmun, calculate actual cost since we only can go below
            if current_column + 1 == (n-1):
                below_actual_path_cost = 0
                for index in range(current_row, n):
                    below_actual_path_cost += grid[index][current_column + 1]
                right_path_cost = path_cost_so_far + below_actual_path_cost
                right_feasible_cost = path_cost_so_far + below_actual_path_cost
            # otherwise calculate current path + heuristic cost, similar to A* search
            else:
                right_path_cost = path_cost_so_far + right_room_cost + heuristic_cost
                right_feasible_cost = right_room_cost + heuristic_cost - 1
        else:
            right_path_cost = 0

        if current_row + 1 < n:
            below_room_cost = grid[current_row + 1][current_column]

            # if last row, calculate actual cost since we only can go right
            if current_row + 1 == (n-1):
                right_actual_path_cost = 0
                for index in range(current_column, n):
                    right_actual_path_cost += grid[current_row + 1][index]
                below_path_cost = path_cost_so_far + right_actual_path_cost
                below_feasible_cost = below_room_cost + right_actual_path_cost
            else:
                below_path_cost = path_cost_so_far + below_room_cost + heuristic_cost
                below_feasible_cost = below_room_cost + heuristic_cost - 1
        else:
            below_path_cost = 0

        if right_path_cost > below_path_cost and right_feasible_cost < food:
            current_column += 1
            path_cost_so_far += right_room_cost
            food -= right_room_cost
        elif right_path_cost < below_path_cost and below_feasible_cost < food:
            current_row += 1
            path_cost_so_far += below_room_cost
            food -= below_room_cost
        elif right_feasible_cost <= food:
            current_column += 1
            path_cost_so_far += right_room_cost
            food -= right_room_cost
        else:
            current_row += 1
            path_cost_so_far += below_room_cost
            food -= below_room_cost

        heuristic_cost -= 1

        if (current_column == (n-1) and current_row == (n-1)) or food < 0:
            zombie_sucks = False

    return food


food1 = 7
grid1 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
print answer(food1, grid1)
# 0

food2 = 12
grid2 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
print answer(food2, grid2)
# 1

food2 = 12
grid2 = [[0, 2, 5], [1, 1, 5], [2, 1, 1]]
print answer(food2, grid2)