def read_input(file_path: str) -> list:
    """
    Read an input of the following format and return a list of
    integer.
    Format:
    125 17
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [int(c) for line in lines for c in line.split(" ")]
    

def get_number_digits(n: int) -> int:
    return len(str(n))

def split_number(n: int) -> list:
    """
    Split a number with even number of digits into two number based on digits on the right and on the left.
    """
    s = str(n)
    n = len(s)
    return [int(s[:n//2]), int(s[n//2:])]

def blink_stone(stone: int) -> list:
    if stone == 0:
        return [1]
    elif get_number_digits(stone) % 2 == 0:
        return split_number(stone)
    else:
        return [stone*2024]


### Naive implementation
def blink_list(current_list: list) -> list:
    """
    Blink the lights.
    """
    new_list = []
    for i in range(len(current_list)):
        new_list = new_list + blink_stone(current_list[i])
    return new_list
    
def get_problem_1(problem: list) -> int:
    """
    Get the number of stones after the 2024th blink.
    """
    current_list = problem
    for i in range(25):
        current_list = blink_list(current_list)
    return len(current_list)


def get_stone_memory_address(stone: int, depth: int) -> int:
    return f"{stone}-{depth}"


memory = {}

### optimized implementation with memory
def problem_2(problem: list, depth = 25) -> int:
    """
    We will create a memory to remember number already processed.
    """
    current_list = problem
    if depth == 0:
        return len(current_list)
    score_tot = 0
    for j in range(len(current_list)):
        if get_stone_memory_address(current_list[j], depth) in memory:
            print(f"Memory hit for {current_list[j]} at depth {depth} and score {memory[get_stone_memory_address(current_list[j], depth)]}")
            score_tot += memory[get_stone_memory_address(current_list[j], depth)]
        else:
            print(f"Memory miss for {current_list[j]} at depth {depth} going to next depth with {blink_stone(current_list[j])}")
            score = problem_2(blink_stone(current_list[j]), depth - 1)
            memory[get_stone_memory_address(current_list[j], depth)] = score
            score_tot += score
    return score_tot
    


def main():
    problem = read_input("2024/day_11/input.txt")
    print(problem)

    probleme_1_solution = problem_2(problem, 25)
    print(f"Problem 1 solution is {probleme_1_solution}")

    probleme_2_solution = problem_2(problem, 75)
    print(f"Problem 2 solution is {probleme_2_solution}")

    # print(f"Memory: {memory}")


main()