

def read_input(file_path):
    """
    Read an input of the form:
    p=0,4 v=3,-3
    p=6,3 v=-1,-3
    p=10,3 v=-1,2
    p=2,0 v=2,-1
    p=0,0 v=1,3
    p=3,0 v=-2,-2
    p=7,6 v=-1,-3
    p=3,0 v=-1,-2
    p=9,3 v=2,3
    p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3

    into a list of p and v tuples.
    """
    with open(file_path, "r") as file:
        return [
            {
                "p": (int(line.split(",")[0].split("p=")[-1]), int(line.split(",")[1].split(" ")[0])),
                "v": (int(line.split(",")[1].split("v=")[-1]), int(line.split(",")[2])),
            }
            for line in file.readlines()
        ]
    

def get_position_after_time(p, v, t, grid_size):
    """
    Given a position p, velocity v and time t, and the grid size return the position after t seconds.
    """
    x = (p[0] + v[0] * t) % grid_size[0]    
    y = (p[1] + v[1] * t) % grid_size[1]
    return x, y

def get_quadrant_product(after_simulation, grid_size):

    q_top_left, q_top_right, q_bottom_left, q_bottom_right = 0, 0, 0, 0
    for r in after_simulation:
        if r["p"][0] < grid_size[0] // 2 and r["p"][1] < grid_size[1] // 2:
            q_top_left += 1
        elif r["p"][0] > grid_size[0] // 2 and r["p"][1] < grid_size[1] // 2:
            q_top_right += 1
        elif r["p"][0] < grid_size[0] // 2 and r["p"][1] > grid_size[1] // 2:
            q_bottom_left += 1
        elif r["p"][0] > grid_size[0] // 2 and r["p"][1] > grid_size[1] // 2:
            q_bottom_right += 1

    print(f"Top Left: {q_top_left}, Top Right: {q_top_right}, Bottom Left: {q_bottom_left}, Bottom Right: {q_bottom_right}")
    return q_top_left * q_top_right * q_bottom_left * q_bottom_right

def display_grid(after_simulation, grid_size):
    grid = [["." for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    for r in after_simulation:
        if grid[r["p"][1]][r["p"][0]] == ".":
            grid[r["p"][1]][r["p"][0]] = 1
        else:
            grid[r["p"][1]][r["p"][0]] += 1

    grid_display = [[str(grid[i][j]) for j in range(grid_size[0])] for i in range(grid_size[1])]
    for r in grid_display:
        print("".join(r))

def problem_1(problem, size, time):
    after_simulation = []
    for r in problem:
        x, y = get_position_after_time(r["p"], r["v"], time, size)
        print(f"Position for {r['p']} after {time}  seconds: {x, y}")
        after_simulation.append({"p": (x, y), "v": r["v"], "initial": r["p"]})

    return get_quadrant_product(after_simulation, size)


def looks_like_tree(after_simulation, grid_size):
    """
    Check if the points are forming a tree.
    """
    grid = [["." for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    for r in after_simulation:
        if grid[r["p"][1]][r["p"][0]] == ".":
            grid[r["p"][1]][r["p"][0]] = 1
        else:
            grid[r["p"][1]][r["p"][0]] += 1

    # check bottom
    nb_robots = 0
    for i in range(grid_size[1]):
        nb_robots = 0
        if grid[i][grid_size[0]-1] != ".":
            nb_robots += 1

    if nb_robots == 3:
        return True
    return False


def problem_2(problem, size):
    after_simulation = []
    time = 1
    while not looks_like_tree(after_simulation, size) or time > 20000:
        after_simulation = []
        print(f'After {time} seconds')
        for r in problem:
            x, y = get_position_after_time(r["p"], r["v"], time, size)
            after_simulation.append({"p": (x, y), "v": r["v"], "initial": r["p"]})
        display_grid(after_simulation, size)
        time += 1

def main():
    file_path = "2024/day_14/input.txt"
    problem = read_input(file_path)
    size_base = (11,7)
    size_input = (101,103)

    print(f"Problem Def {problem}")

    res_1 = problem_1(problem, size_input, 100)
    print(f"Problem 1: {res_1}")

    problem_2(problem, size_input)



main()