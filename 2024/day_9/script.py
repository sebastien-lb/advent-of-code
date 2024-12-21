

def read_input(file_path: str) -> list:
    """
    Read an input of the following format and return a list of list of
    characters.
    Format:
    2333133121414131402
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [int(c) for line in lines for c in line.strip()]
    
def create_disk_arrangement(problem: list) -> list:
    """
    Create a disk arrangement of n disks.
    """
    disks = []
    is_memory = False
    file_id = 0
    for i in range(len(problem)):
        size = int(problem[i])
        if not is_memory:
            disks = disks + [file_id] * size
            file_id += 1
        else:
            disks = disks + ["."] * size
        is_memory = not is_memory
    return disks

def re_index_disks(disks: list) -> list:
    new_disks = [a for a in disks]
    n = len(new_disks)
    bottom_cursor = 0
    top_cursor = n - 1
    while bottom_cursor < top_cursor:
        if new_disks[bottom_cursor] == "." and new_disks[top_cursor] != ".":
            # switch
            new_disks[bottom_cursor], new_disks[top_cursor] = new_disks[top_cursor], new_disks[bottom_cursor]
        elif new_disks[bottom_cursor] == "." and new_disks[top_cursor] == ".":
            top_cursor -= 1
        elif new_disks[bottom_cursor] != ".":
            bottom_cursor += 1
    return new_disks

def get_disk_checksum(disks: list) -> int:
    s = 0
    for i in range(len(disks)):
        if disks[i] != ".":
            s += i*int(disks[i])
    return s

## Part 2


def get_free_space_size(disks: list, index: int) -> int:
    """
    Get the size of the free space starting from the index.
    """
    size = 0
    for i in range(index, len(disks)):
        if disks[i] == ".":
            size += 1
        else:
            break
    return size

def get_file_size_reverse(disks: list, index: int) -> int:
    """
    Get the size of the free space starting from the index.
    """
    size = 0
    first = disks[index]
    for i in range(index):
        if disks[index-i] == first:
            size += 1
        else:
            break
    return size

def get_problem_2_new_disk(disks: list):
    new_disks = [a for a in disks]
    n = len(new_disks)
    current_file_id = max([int(c) for c in new_disks if c != "."])
    for i in range(n):
        if new_disks[n-1-i] == current_file_id:
            size_file = get_file_size_reverse(new_disks, n-1-i)
            for j in range(n-1-i):
                if new_disks[j] == ".":
                    size_space = get_free_space_size(new_disks, j)
                    if size_space >= size_file:
                        # print(f"Switch index {i} {j} for current file {current_file_id} and size {size_file}")
                        # print(f"Disk before switch: {new_disks}")
                        # print(f"Block to back: {new_disks[n-i-size_file:n-i]}")
                        new_disks[j:j+size_file] = new_disks[n-i-size_file:n-i]
                        new_disks[n-i-size_file:n-i] = ["."] * size_file
                        # print(f"Disk after switch: {new_disks}")
                        break
            current_file_id -= 1
    return new_disks


def main():
    problem = read_input("2024/day_9/input.txt")
    print(f"Problem: {problem}")
    
    
    disks = create_disk_arrangement(problem)
    print(f"Disks: {disks}")

    new_disks = re_index_disks(disks)
    print(f"New disks: {new_disks}")

    checksum = get_disk_checksum(new_disks)
    print(f"Checksum: {checksum}")

    new_disks_2 = get_problem_2_new_disk(disks)
    print(f"New disks 2: {new_disks_2}")
    checksum_2 = get_disk_checksum(new_disks_2)
    print(f"Checksum 2: {checksum_2}")

main()