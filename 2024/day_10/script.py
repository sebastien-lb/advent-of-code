

def read_input(file_path: str) -> list:
    """
    Read an input of the following format and return a list of list of
    integer.
    Format:
    0123
    1234
    8765
    9876
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [[int(c) for c in line.strip()] for line in lines]
    

def find_initial_position(problem: list) -> list:
    """
    Find the initial position of the robot.
    """
    rep = []
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if problem[i][j] == 0:
                rep.append((i, j))
    return rep

def get_sumbit_reachable(problem: list, position: list) -> list:
    """
    Get the number of submit reachable by the robot.
    """
    if problem[position[0]][position[1]] == 9:
        # we are at the top
        return [position]
    current_elevation = problem[position[0]][position[1]]
    possible_positions = []
    if position[0] > 0:
        possible_positions.append((position[0]-1, position[1]))
    if position[0] < len(problem) - 1:
        possible_positions.append((position[0]+1, position[1]))
    if position[1] > 0:
        possible_positions.append((position[0], position[1]-1))
    if position[1] < len(problem[0]) - 1:
        possible_positions.append((position[0], position[1]+1))

    rep = []
    for pos in possible_positions:
        if problem[pos[0]][pos[1]] == current_elevation + 1:
            print(f"advancing form position {position} of elevation {problem[position[0]][position[1]]} to {pos} of elevation {problem[pos[0]][pos[1]]}")
            rep = rep + get_sumbit_reachable(problem, pos)
    return rep

def get_position_str(position):
    return f"{position[0]}-{position[1]}"

def get_problem_1(problem):
    initial_positions = find_initial_position(problem)
    s = 0
    for pos in initial_positions:
        print(f"Initial position: {pos}")
        reachable_submit = get_sumbit_reachable(problem, pos)
        diff = {}
        for submit in reachable_submit:
            print(f"Submit: {submit}")
            if get_position_str(submit) not in diff:
                diff[get_position_str(submit)] = 1
            else:
                diff[get_position_str(submit)] += 1
        score_pos = len(diff)
        print(f"Score pos: {score_pos}")
        s += score_pos
    return s

def get_problem_2(problem):
    initial_positions = find_initial_position(problem)
    s = 0
    for pos in initial_positions:
        print(f"Initial position: {pos}")
        reachable_submit = get_sumbit_reachable(problem, pos)
        score_pos = len(reachable_submit)
        print(f"Score pos: {score_pos}")
        s += score_pos
    return s


def main():
    problem = read_input("2024/day_10/input.txt")
    number_of_reachable_submit = get_problem_1(problem)

    print(f"Problem 1: {number_of_reachable_submit}")

    number_of_reachable_submit_2 = get_problem_2(problem)

    print(f"Problem 2: {number_of_reachable_submit_2}")

main()