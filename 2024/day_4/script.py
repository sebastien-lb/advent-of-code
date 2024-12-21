


def read_input(file_path: str) -> list:
    with open(file_path, "r") as file:
        lines = file.readlines()
        return lines
    
def get_nb_xmas(lines: list) -> int:
    """
        Get the number of xmas in the list
    """
    nb_xmas = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # XMAS
            if j+3 < len(lines[i]) and lines[i][j:j+4] == "XMAS":
                nb_xmas += 1
            # SAMX
            if j >= 3 and lines[i][j-4:j] == "SAMX":
                nb_xmas += 1
            # X
            # M
            # A
            # S
            if i + 3 < len(lines) and lines[i][j] == "X" and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
                nb_xmas += 1
            # S
            # A
            # M
            # X
            if i >= 3 and lines[i][j] == "X" and lines[i-1][j] == "M" and lines[i-2][j] == "A" and lines[i-3][j] == "S":
                nb_xmas += 1
            # X
            #  M
            #   A
            #    S
            if i + 3 < len(lines) and j + 3 < len(lines[i]) and lines[i][j] == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                nb_xmas += 1
            # S
            #  A
            #   M
            #    X
            if i >= 3 and j >= 3 and lines[i][j] == "X" and lines[i-1][j-1] == "M" and lines[i-2][j-2] == "A" and lines[i-3][j-3] == "S":
                nb_xmas += 1
            #    S
            #   A
            #  M
            # X
            if i >= 3 and j + 3 < len(lines[i]) and lines[i][j] == "X" and lines[i-1][j+1] == "M" and lines[i-2][j+2] == "A" and lines[i-3][j+3] == "S":
                nb_xmas += 1
            #    X
            #   M
            #  A
            # S
            if i + 3 < len(lines) and j >= 3 and lines[i][j] == "X" and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                nb_xmas += 1

    return nb_xmas


def get_nb_xmas_cross(lines: list) -> int:
    nb_xmas = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            #  M S
            #   A
            #  M S
            if i + 2 < len(lines) and j + 2 < len(lines[i]) and lines[i][j] == "M" and lines[i][j+2] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j] == "M" and lines[i+2][j+2] == "S":
                nb_xmas += 1
            #  S S
            #   A
            #  M M
            if i + 2 < len(lines) and j + 2 < len(lines[i]) and lines[i][j] == "S" and lines[i][j+2] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j] == "M" and lines[i+2][j+2] == "M":
                nb_xmas += 1
            #  S M
            #   A
            #  S M
            if i + 2 < len(lines) and j + 2 < len(lines[i]) and lines[i][j] == "S" and lines[i][j+2] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j] == "S" and lines[i+2][j+2] == "M":
                nb_xmas += 1
            #  M M
            #   A
            #  S S
            if i + 2 < len(lines) and j + 2 < len(lines[i]) and lines[i][j] == "M" and lines[i][j+2] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j] == "S" and lines[i+2][j+2] == "S":
                nb_xmas += 1
    return nb_xmas

            

def main():
    lines = read_input("2024/day_4/input.txt")
    print(f"Number of lines: {len(lines)} {lines[0]}")
    nb_xmas = get_nb_xmas(lines)
    print(f"Number of xmas: {nb_xmas}")
    nb_xmas_cross = get_nb_xmas_cross(lines)
    print(f"Number of xmas cross: {nb_xmas_cross}")

main()