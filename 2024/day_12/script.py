from functools import cmp_to_key

def read_input(file_path: str) -> list:
    """
    Read an input of the following format and return a list of list of strings.

    Format:
    RRRRIICCFF
    RRRRIICCCF
    VVRRRCCFFF
    VVRCCCJFFF
    VVVVCJJCFE
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [[c for c in line.strip()] for line in lines]
    

def get_all_different_type(problem: list) -> list:
    """
    Get all the different type of rooms in the problem.
    """
    rep = {}
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            rep[problem[i][j]] = True
    return list(rep.keys())

def get_similar_neighbor_of_point(problem: list, pos) -> list:
    """
    Get the similar neighbors of a point.
    """
    i, j = pos
    rep = []
    if i > 0 and problem[i-1][j] == problem[i][j]:
        rep.append((i-1, j))
    if i < len(problem) - 1 and problem[i+1][j] == problem[i][j]:
        rep.append((i+1, j))
    if j > 0 and problem[i][j-1] == problem[i][j]:
        rep.append((i, j-1))
    if j < len(problem[i]) - 1 and problem[i][j+1] == problem[i][j]:
        rep.append((i, j+1))
    return rep


def get_pos_str(pos) -> str:
    return f"{pos[0]}-{pos[1]}"

def get_region_of_point(problem: list, pos, region = {}) -> list:
    """
    Get the region of a point.
    """
    region[get_pos_str(pos)] = True
    similar = get_similar_neighbor_of_point(problem, pos)

    not_visited = [sim for sim in similar if get_pos_str(sim) not in region]

    if not_visited == []:
        return region
    
    new_region = {**region}
    for sim in not_visited:
        new_region[get_pos_str(sim)] = True
    for sim in not_visited:
        new_region = {**new_region, **get_region_of_point(problem, sim, new_region)}
    return new_region


def get_regions(problem: list) -> list:
    """
    Get the regions of the problem.
    """
    regions = []
    visited = [[False for _ in range(len(problem[0]))] for _ in range(len(problem))]
    for i in range(len(problem)):
        for j in range(len(problem[0])):
            if not visited[i][j]:
                region = get_region_of_point(problem, (i, j), {})
                # print(f"Region of {(i,j)} - {problem[i][j]} - len {len(region)}  - {region}")
                regions.append(region)
                for k_pos in region.keys():
                    ii, jj = k_pos.split("-")
                    visited[int(ii)][int(jj)] = True
    return regions

def get_region_area(region: list) -> int:
    return len(region)  

def get_region_perimeter(problem, region: list) -> int:
    perimeter = 0
    for pos in region.keys():
        i, j = pos.split("-")
        i, j = int(i), int(j)
        if get_pos_str((i-1, j)) not in region:
            perimeter += 1
        if get_pos_str((i+1, j)) not in region:
            perimeter += 1
        if get_pos_str((i, j-1)) not in region:
            perimeter += 1
        if get_pos_str((i, j+1)) not in region:
            perimeter += 1
    return perimeter


def get_nb_of_side(region: list) -> int:
    """
    Get the number of side of a region.
    """
    sides = []
    for pos in region.keys():
        i, j = pos.split("-")
        i, j = int(i), int(j)
        if get_pos_str((i-1, j)) not in region:
            sides.append([(i, j), "top"])
        if get_pos_str((i+1, j)) not in region:
            sides.append([(i, j), "bottom"])
        if get_pos_str((i, j-1)) not in region:
            sides.append([(i, j), "left"])
        if get_pos_str((i, j+1)) not in region:
            sides.append([(i, j), "right"])


    # we have all the sides

    def fn_sort_top(item1, item2):
        if item1[1] > item2[1]:
            return 1
        elif item1[1] < item2[1]:
            return -1
        if item1[0][0] > item2[0][0]:
            return 1
        elif item1[0][0] < item2[0][0]:
            return -1
        
        if item1[0][1] > item2[0][1]:
            return 1
        elif item1[0][1] < item2[0][1]:
            return -1
        return 0
    
    def fn_sort_left(item1, item2):
        if item1[1] > item2[1]:
            return 1
        elif item1[1] < item2[1]:
            return -1
        
        if item1[0][1] > item2[0][1]:
            return 1
        elif item1[0][1] < item2[0][1]:
            return -1
        
        if item1[0][0] > item2[0][0]:
            return 1
        elif item1[0][0] < item2[0][0]:
            return -1
        return 0

    sides_sorted_1 = sorted(filter(lambda x: x[1] in ["top", "bottom"], sides), key=cmp_to_key(fn_sort_top))
    sides_sorted_2 = sorted(filter(lambda x: x[1] in ["left", "right"], sides), key=cmp_to_key(fn_sort_left))

    previous_side = None
    side_count = 0
    # top bottom
    for side in sides_sorted_1:
        if previous_side is None or previous_side[1] != side[1]:
            previous_side = side
            side_count = side_count + 1
        else:
            if previous_side[0][1] + 1 == side[0][1] and previous_side[0][0] == side[0][0]:
                previous_side = side
            else:
                previous_side = side
                side_count = side_count + 1
    print(f"Sides sorted 1 : {sides_sorted_1}")
    print(f"Sides count sorted 1 : {side_count}")
    mem = side_count
    # left right
    for side in sides_sorted_2:
        if previous_side is None or previous_side[1] != side[1]:
            previous_side = side
            side_count = side_count + 1
        else:
            if previous_side[0][0] + 1 == side[0][0] and previous_side[0][1] == side[0][1]:
                previous_side = side
            else:
                previous_side = side
                side_count = side_count + 1

    
    print(f"Sides sorted 2 : {sides_sorted_2}")
    print(f"Sides count sorted 2 : {side_count - mem}")
    # count sides hor 

    return side_count


def get_problem_1(problem: list) -> int:
    """
    Get the area of the largest region.
    """
    regions = get_regions(problem)
    score = 0
    for region in regions:
        area = get_region_area(region)
        perimeter = get_region_perimeter(problem, region)
        print(f"Region:  - Area: {area} - Perimeter: {perimeter}")
        score += area*perimeter
    return score

def get_problem_2(problem: list) -> int:
    """
    Get the area of the largest region.
    """
    regions = get_regions(problem)
    score = 0
    for region in regions:
        area = get_region_area(region)
        nb_sides = get_nb_of_side(region)
        print(f"Region:  - Area: {area} - Sides: {nb_sides}")
        score += area*nb_sides
    return score

def main():
    problem = read_input("2024/day_12/input.txt")
    print(f"Problem: {problem}")

    score_pbm_1 = get_problem_1(problem)
    print(f"Problem 1: {score_pbm_1}")

    score_pbm_2 = get_problem_2(problem)
    print(f"Problem 2: {score_pbm_2}")

main()