

def read_input(file_path: str) -> list:
    """
    Read an input of the form:
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176

    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450

    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279

    and return a list of dict:
    [{"A": (94, 34), "B": (22, 67), "Prize": (8400, 5400)}, ...]
    """
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n\n")

    return [
        {
            "A": (int(line.split("\n")[0].split("X+")[1].split(",")[0]), int(line.split("\n")[0].split("Y+")[-1])),
            "B": (int(line.split("\n")[1].split("X+")[1].split(",")[0]), int(line.split("\n")[1].split("Y+")[-1])),
            "Prize": (int(line.split("\n")[2].split("X=")[1].split(",")[0]), int(line.split("\n")[2].split("Y=")[-1])),
        }
        for line in data
    ] 


def solve_system(a, b, c, d, e, f):
    """
    Solve a system of equations of the form:
    a*x + b*y = e
    c*x + d*y = f
    --- 
    c (a*x + b*y)  = c*e
    a * (c*x + d*y)  = a*f
    --- > (1) / (2) - (1)
    c (a*x + b*y)  = c*e
    (ad - bc ) * y = af - ce
    ---
    y = (af - ce) / (ad - bc)
    ###
    d (a*x + b*y)  = d*e
    b * (c*x + d*y)  = b*f
    --- > (1) / (1) - (2)
    (ad - bc) * x = de - bf
    ---
    x = (de - bf) / (ad - bc)
    """
    det = a * d - b * c
    if det == 0:
        return None
    x = (e * d - b * f) / det
    y = (a * f - e * c) / det

    print(f"Solution for the system is : {(x, y)}")
    return x, y


def problem_1(problem):
    """
    Given a list of dict of the form:
    [{"A": (X, Y), "B": (X, Y), "Prize": (X, Y)}, ...]

    Determine if the prize location is reachable from the buttons and the number fo steps.
    """
    rep = [
        solve_system(
            p["A"][0],
            p["B"][0],
            p["A"][1],
            p["B"][1],
            p["Prize"][0],
            p["Prize"][1],
        )
        for p in problem
    ]

    # filter integer solutions

    solutions = [r for r in rep if r is not None and all([int(x) == x for x in r])]

    return sum([3*r[0]+r[1] for r in solutions if r is not None])

def main():
    file_path = "2024/day_13/input.txt"
    problem = read_input(file_path)

    print(problem)
    print(f"Problem 1: {problem_1(problem)}")

    error = 10000000000000
    problem2 = [
        {"A": p["A"], "B": p["B"], "Prize": (p["Prize"][0] + error , p["Prize"][1] + error)}
        for p in problem        
    ]

    print(f"Problem 2: {problem_1(problem2)}")


main()


    