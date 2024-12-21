

def read_input(file_path):
    """
    Read an input if the following form. Return a grid of initial positions and a list of moves.
    ##########
    #..O..O.O#
    #......O.#
    #.OO..O.O#
    #..O@..O.#
    #O#..O...#
    #O..O..O.#
    #.OO.O.OO#
    #....O...#
    ##########

    <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
    vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
    ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
    <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
    ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
    ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
    >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
    <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
    ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
    v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
    """

    with open(file_path, "r") as file:
        data = file.read().strip().split("\n\n")

    data_grid = data[0].split("\n")
    data_moves = data[1].split("\n")
    
    grid = [[c for c in d] for d  in data_grid ]
    moves = [c for d in data_moves for c in d ]

    return grid, moves

def get_robot_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return i, j
    return None

def get_next_available_box_place(grid, robot_position, move):
    """
    Given a grid and the robot position, return the move to make the box move.
    """
    if move == "v":
        j = 1
        while grid[robot_position[0] + j][robot_position[1]] == "O" and j < 2*len(grid):
            j += 1
        if grid[robot_position[0] + j][robot_position[1]] == ".":
            return robot_position[0] + j, robot_position[1]
        if grid[robot_position[0] + j][robot_position[1]] == "#":
            return None
    if move == "^":
        j = 1
        while grid[robot_position[0] - j][robot_position[1]] == "O" and j < 2*len(grid):
            j += 1
        if grid[robot_position[0] - j][robot_position[1]] == ".":
            return robot_position[0] - j, robot_position[1]
        if grid[robot_position[0] - j][robot_position[1]] == "#":
            return None
    if move == ">":
        j = 1
        while grid[robot_position[0]][robot_position[1] + j] == "O" and j < 2*len(grid):
            j += 1
        if grid[robot_position[0]][robot_position[1] + j] == ".":
            return robot_position[0], robot_position[1] + j
        if grid[robot_position[0]][robot_position[1] + j] == "#":
            return None
    if move == "<":
        j = 1
        while grid[robot_position[0]][robot_position[1] - j] == "O" and j < 2*len(grid):
            j += 1
        if grid[robot_position[0]][robot_position[1] - j] == ".":
            return robot_position[0], robot_position[1] - j
        if grid[robot_position[0]][robot_position[1] - j] == "#":
            return None
    return None

def move_robot_on_grid(grid, move, robot_position):
    """
    No need to check for out of bound because input has a security barrier.
    """
    new_grid = [[c for c in d] for d in grid]
    if move == "v":
        if grid[robot_position[0] + 1][robot_position[1]] == "#":
            return new_grid, robot_position
        elif grid[robot_position[0] + 1][robot_position[1]] == ".":
            return new_grid, (robot_position[0] + 1, robot_position[1])
        elif grid[robot_position[0] + 1][robot_position[1]] == "O":
            # Logic for moving the box.
            next_box_place = get_next_available_box_place(grid, robot_position, move)
            if next_box_place is not None:
                new_grid[robot_position[0] + 1][robot_position[1]] = "."
                new_grid[next_box_place[0]][next_box_place[1]] = "O"
                return new_grid, (robot_position[0] + 1, robot_position[1])
            else:
                # can't move the box
                return new_grid, robot_position
    elif move == "^":
        if grid[robot_position[0] - 1][robot_position[1]] == "#":
            return new_grid, robot_position
        elif grid[robot_position[0] - 1][robot_position[1]] == ".":
            return new_grid, (robot_position[0] - 1, robot_position[1])
        elif grid[robot_position[0] - 1][robot_position[1]] == "O":
            # Logic for moving the box.
            next_box_place = get_next_available_box_place(grid, robot_position, move)
            if next_box_place is not None:
                new_grid[robot_position[0] - 1][robot_position[1]] = "."
                new_grid[next_box_place[0]][next_box_place[1]] = "O"
                return new_grid, (robot_position[0] - 1, robot_position[1])
            else:
                # can't move the box
                return new_grid, robot_position
    elif move == ">":
        if grid[robot_position[0]][robot_position[1] + 1] == "#":
            return new_grid, robot_position
        elif grid[robot_position[0]][robot_position[1] + 1] == ".":
            return new_grid, (robot_position[0], robot_position[1] + 1)
        elif grid[robot_position[0]][robot_position[1] + 1] == "O":
            # Logic for moving the box.
            next_box_place = get_next_available_box_place(grid, robot_position, move)
            if next_box_place is not None:
                new_grid[robot_position[0]][robot_position[1] + 1] = "."
                new_grid[next_box_place[0]][next_box_place[1]] = "O"
                return new_grid, (robot_position[0], robot_position[1] + 1)
            else:
                # can't move the box
                return new_grid, robot_position
    elif move == "<":
        if grid[robot_position[0]][robot_position[1] - 1] == "#":
            return new_grid, robot_position
        elif grid[robot_position[0]][robot_position[1] - 1] == ".":
            return new_grid, (robot_position[0], robot_position[1] - 1)
        elif grid[robot_position[0]][robot_position[1] - 1] == "O":
            # Logic for moving the box.
            next_box_place = get_next_available_box_place(grid, robot_position, move)
            if next_box_place is not None:
                new_grid[robot_position[0]][robot_position[1] - 1] = "."
                new_grid[next_box_place[0]][next_box_place[1]] = "O"
                return new_grid, (robot_position[0], robot_position[1] - 1)
            else:
                # can't move the box
                return new_grid, robot_position
    print(f"Move {move} is not valid.")
    return None

def get_grid_score(grid):

    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                score += i*100 + j
    return score

def problem_1(grid, moves):
    initial_position = get_robot_position(grid)

    grid[initial_position[0]][initial_position[1]] = "." 

    position = initial_position
    for m in moves:
        grid, position = move_robot_on_grid(grid, m, position)
    return get_grid_score(grid)


def problem_2(grid, moves):
    # TODO: Implement problem 2
    return None

def main():
    grid, moves = read_input("2024/day_15/input.txt")
    print(f"Grid: {grid}")
    print(f"Moves: {moves}")

    score_1 = problem_1(grid, moves)
    print(f"Problem 1: {score_1}")

main()