

def read_input(file_path):
    """
    Read an input of the form:
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............
    """
    with open(file_path) as file:
        lines = file.readlines()
        return [[c for c in line.strip()] for line in lines]
    

def compute_antinode_nb(an_type: str, problem: list) -> int:
    """
    Compute the number of antinodes of a given type in the problem.
    """
    height = len(problem)
    length = len(problem[0])

    all_an_types = []
    an_locations = {}
    for i in range(height):
        for j in range(length):
            if problem[i][j] == an_type:
                all_an_types.append((i, j))
    
    for i in range(len(all_an_types)):
        for j in range(i+1, len(all_an_types)):
            an_1, an_2 = all_an_types[i], all_an_types[j]
            an_loc = compute_antinode_location(an_1, an_2, height, length)
            for an in an_loc:
                an_locations[get_an_notation(an)] = True
    return len(an_locations), an_locations

def get_an_notation(an):
    return f"{an[0]}_{an[1]}"

def compute_antinode_location(position_1, position_2, height, length):
    """
    Compute the location of the antinode.
    """
    diff = abs(position_1[0] - position_2[0]), abs(position_1[1] - position_2[1])
    an_1, an_2 = None, None

    if diff[0] == 0:
        # Align vertically
        if position_1[1] < position_2[1]:
            an_1 = position_1[0], position_1 - diff[1]
            an_2 = position_2[0], position_2 + diff[1] 
        elif position_1[1] > position_2[1]:
            an_1 = position_1[0], position_1 + diff[1]
            an_2 = position_2[0], position_2 - diff[1]
        else:
            print("Unexpected two an at the same position")
            return None, None
    elif diff[1] == 0:
        # Align horizontally
        if position_1[0] < position_2[0]:
            an_1 = position_1[0] - diff[0], position_1[1]
            an_2 = position_2[0] + diff[0], position_2[1]
        elif position_1[0] > position_2[0]:
            an_1 = position_1[0] + diff[0], position_1[1]
            an_2 = position_2[0] - diff[0], position_2[1]
        else:
            print("Unexpected two an at the same position")
            return None, None
    else:
        # general case
        if position_1[0] < position_2[0]:
            if position_1[1] < position_2[1]:
                an_1 = position_1[0] - diff[0], position_1[1] - diff[1]
                an_2 = position_2[0] + diff[0], position_2[1] + diff[1]
            elif position_1[1] > position_2[1]:
                an_1 = position_1[0] - diff[0], position_1[1] + diff[1]
                an_2 = position_2[0] + diff[0], position_2[1] - diff[1]
        elif position_1[0] > position_2[0]:
            if position_1[1] < position_2[1]:
                an_1 = position_1[0] + diff[0], position_1[1] - diff[1]
                an_2 = position_2[0] - diff[0], position_2[1] + diff[1]
            elif position_1[1] > position_2[1]:
                an_1 = position_1[0] + diff[0], position_1[1] + diff[1]
                an_2 = position_2[0] - diff[0], position_2[1] - diff[1]
    
    # filter out the ones that are out of bounds
    if an_1[0] < 0 or an_1[0] >= height or an_1[1] < 0 or an_1[1] >= length:
        an_1 = None
    if an_2[0] < 0 or an_2[0] >= height or an_2[1] < 0 or an_2[1] >= length:
        an_2 = None
    
    rep = []
    if an_1:
        rep.append(an_1)
    if an_2:
        rep.append(an_2)
    return rep


def compute_antinode_location_2(position_1, position_2, height, length):
    """
    Compute the location of the antinode.
    """
    diff = (position_1[0] - position_2[0], position_1[1] - position_2[1])

    an_list = [(position_1[0] + k*diff[0], position_1[1] + k*diff[1]) for k in range(-max(length,height), max(height, length))]
    
    # filter out the ones that are out of bounds
    an_list = [an for an in an_list if an[0] >= 0 and an[0] < height and an[1] >= 0 and an[1] < length]
    
    return an_list

def compute_antinode_nb_2(an_type: str, problem: list) -> int:
    """
    Compute the number of antinodes of a given type in the problem part 2.
    """
    height = len(problem)
    length = len(problem[0])

    all_an_types = []
    an_locations = {}
    for i in range(height):
        for j in range(length):
            if problem[i][j] == an_type:
                all_an_types.append((i, j))
    
    for i in range(len(all_an_types)):
        for j in range(i+1, len(all_an_types)):
            an_1, an_2 = all_an_types[i], all_an_types[j]
            an_loc = compute_antinode_location_2(an_1, an_2, height, length)
            for an in an_loc:
                an_locations[get_an_notation(an)] = True
    return len(an_locations), an_locations


def get_all_an_type(problem):
    types = {}
    for i in range(len(problem)):
        for j in range(len(problem[0])):
            if problem[i][j] != "." and problem[i][j] not in types:
                types[problem[i][j]] = True
    return types.keys()

def get_pbm_1(problem):
    all_an_types = get_all_an_type(problem)
    print(f"All An types: {all_an_types}")

    all_an_loc = {}
    for an_type in all_an_types:
        sum_par, an_loc = compute_antinode_nb(an_type, problem)
        print(f"Type {an_type} | antinodes nb: {sum_par} | antinodes loc: {an_loc}")
        for k in an_loc.keys():
            all_an_loc[k] = True

    return len(all_an_loc)

def get_pbm_2(problem):
    all_an_types = get_all_an_type(problem)
    print(f"All An types: {all_an_types}")

    all_an_loc = {}
    for an_type in all_an_types:
        sum_par, an_list = compute_antinode_nb_2(an_type, problem)
        print(f"Type {an_type} | antinodes nb: {sum_par} | antinodes loc: {an_list}")
        for k in an_list:
            all_an_loc[k] = True

    return len(all_an_loc)


def main():
    problem = read_input("2024/day_8/input.txt")
    print(f"Problem: {problem}")

    print("Basic checks")
    loc = compute_antinode_location((3, 4), (5, 5), 10, 10)
    print("Location: ", loc)

    sum_an = get_pbm_1(problem)
    print(f"Number of antinodes: {sum_an}")

    sum_an_2 = get_pbm_2(problem)
    print(f"Number of antinodes with 2: {sum_an_2}")

main()