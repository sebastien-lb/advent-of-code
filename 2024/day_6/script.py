

def read_input(file_path: str) -> list:
    """
    Read an input of the following format and return a list of list of characters.
    Format:
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [[ c for c in line.strip()] for line in lines]
    

def get_guard_position(problem: list):
    """
    Get the position of the guard.
    """
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if problem[i][j] == '^':
                return (i, j)
    return None

def get_problem_without_guard(problem: list):
    """
    Remove the guard ^ from the problem
    """
    return [[ '.' if c == "^" else c for c in line] for line in problem]

def get_next_position_and_direction(problem: list, guard_position, direction: str):
    """
    Get the next position of the guard and the direction.
    Direction can be: 'left', 'right', 'up', 'down'
    """
    i, j = guard_position
    if direction == 'left':
        if j == 0 :
            return None, 'left'
        if problem[i][j-1] == '.':
            return (i, j-1), 'left'
        if problem[i][j-1] == '#':
            return (i, j), 'up'
    if direction == 'right':
        if j == len(problem[i]) - 1:
            return None, 'right'
        if problem[i][j+1] == '.':
            return (i, j+1), 'right'
        if problem[i][j+1] == '#':
            return (i, j), 'down'
    if direction == 'up':
        if i == 0:
            return None, 'up'
        if problem[i-1][j] == '.':
            return (i-1, j), 'up'
        if problem[i-1][j] == '#':
            return (i, j), 'right'
    if direction == 'down':
        if i == len(problem) - 1:
            return None, 'down'
        if problem[i+1][j] == '.':
            return (i+1, j), 'down'
        if problem[i+1][j] == '#':
            return (i, j), 'left'
    print(f"Error: {i} {j} {direction}")
    return None, None
        
def get_position_code(i, j):
    return f"{i}-{j}"  

def get_nb_position(problem: list) -> int:
    """
    Get the number of position on which the guard will go.
    """
    guard_position = get_guard_position(problem)
    problem = get_problem_without_guard(problem)
    guard_next_position, direction = get_next_position_and_direction(problem, guard_position, 'up')
    visited = {}
    visited[get_position_code(guard_position[0], guard_position[1])] = ["up"]
    visited[get_position_code(guard_next_position[0], guard_next_position[1])] = [direction]

    print(f'Initial guard position: {guard_position}')
    print(f'First move: {guard_next_position}')
    print(f'Visited: {visited}')

    while guard_next_position is not None:
        guard_next_position, direction = get_next_position_and_direction(problem, guard_next_position, direction)
        print(f'Next move: {guard_next_position} {direction}')
        if guard_next_position is None:
            break
        if is_in_loop(visited, guard_next_position, direction):
            return None
        # Add previous to the visited position
        if get_position_code(guard_next_position[0], guard_next_position[1]) not in visited:
            visited[get_position_code(guard_next_position[0], guard_next_position[1])] = [direction]
        else:
            visited[get_position_code(guard_next_position[0], guard_next_position[1])] = visited[get_position_code(guard_next_position[0], guard_next_position[1])] + [direction]
    
    # print(f'Visited: {visited}')
    return len(visited)


def process_walk(problem: list, guard_next_position: tuple, direction: str, visited_previous: dict):
    """
    Process the walk of the guard.
    """
    # guard_next_position, direction = get_next_position_and_direction(problem, guard_position, direction)
    # copy dict
    visited = {k: v for k, v in visited_previous.items()}
    # if get_position_code(guard_next_position[0], guard_next_position[1]) not in visited:
    #     visited[get_position_code(guard_next_position[0], guard_next_position[1])] = [direction]
    # else:
    #     visited[get_position_code(guard_next_position[0], guard_next_position[1])] = visited[get_position_code(guard_next_position[0], guard_next_position[1])] + [direction]

    while guard_next_position is not None:
        guard_next_position, direction = get_next_position_and_direction(problem, guard_next_position, direction)
        if guard_next_position is None:
            break
        if is_in_loop(visited, guard_next_position, direction):
            return None, visited
        # Add previous to the visited position
        if get_position_code(guard_next_position[0], guard_next_position[1]) not in visited:
            visited[get_position_code(guard_next_position[0], guard_next_position[1])] = [direction]
        else:
            visited[get_position_code(guard_next_position[0], guard_next_position[1])] = visited[get_position_code(guard_next_position[0], guard_next_position[1])] + [direction]
    
    #print(f'Visited during walk: {visited}')
    return len(visited), visited


def is_in_loop(visited: dict, position: tuple, direction: str) -> bool:
    """
    Check if a position is in a loop.
    """
    if get_position_code(position[0], position[1]) not in visited:
        return False
    if direction in visited[get_position_code(position[0], position[1])]:
        return True
    else:
        return False


def get_nb_position_loop(problem: list) -> int:
    initial_guard_position = get_guard_position(problem)
    problem = get_problem_without_guard(problem)
    guard_next_position, direction = initial_guard_position, 'up'
    visited = {}
    visited[get_position_code(initial_guard_position[0], initial_guard_position[1])] = ["up"]

    loop_addon_position = {}

    print(f'Initial guard position: {initial_guard_position}')
    print(f'Initial Visited: {visited}')

    initial_walk_length, visited_initial_walk = process_walk(problem, guard_next_position, direction, visited)

    # get coord of initial walk visited
    coord_to_test_obstacle = []
    for k, v in visited_initial_walk.items():
        if int(k.split('-')[0]) != initial_guard_position[0] or int(k.split('-')[1]) != initial_guard_position[1]:
            coord_to_test_obstacle.append((int(k.split('-')[0]), int(k.split('-')[1])))

    print(f"Coord to test obstacle: {len(coord_to_test_obstacle)} - first {coord_to_test_obstacle[:10]}")

    for coord in coord_to_test_obstacle:
        problem_bis = [[c for c in line] for line in problem]
        problem_bis[coord[0]][coord[1]] = '#'
        walk_length, visited_walk = process_walk(problem_bis, initial_guard_position, "up", {})
        if walk_length is not None:
            loop_addon_position[get_position_code(coord[0], coord[1])] = visited_walk

    # remove add on that are already in problem
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if problem[i][j] == '#' and get_position_code(i, j) in loop_addon_position:
                loop_addon_position[get_position_code(i, j)] = False

    nb_false_value = 0
    for k, v in loop_addon_position.items():
        if v is False:
            nb_false_value += 1
    print(f"Nb false value: {nb_false_value}")
    # print(f"Loop addon position: {loop_addon_position}")
    return len(loop_addon_position)

def main():
    problem = read_input("2024/day_6/input.txt")
    nb_position = get_nb_position(problem)
    print(f"Number of position: {nb_position}")

    print(f"Computing Loops")

    # print("Testing process walk")
    # walk, visited_walk = process_walk(get_problem_without_guard(problem), (6, 4), 'up', {})
    # print(f"Walk: {walk}")

    nb_position_loop = get_nb_position_loop(problem)

    print(f"Number of loop possible: {nb_position_loop}")


main()