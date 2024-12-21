

def read_input(file_path: str) -> dict:
    """
    Read a file of the format: 
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20
    """
    with open(file_path, 'r') as file_handle:
        lines = file_handle.readlines()
    
    return {
        int(line.split(':')[0]): list(map(int, line.split(':')[1].strip().split()))
        for line in lines
    }

def can_be_made_true_equation(value, numbers, acc=0,acc_string=""):
    if acc == value and len(numbers) == 0:
        print(f"Equation: {value} == {acc_string}")
        return True
    if acc > value:
        return False
    if len(numbers) == 0:
        return False
    # Explore combinations
    num = numbers[0]
    return can_be_made_true_equation(value, numbers[1:], acc*num, acc_string+"*"+str(num)) or can_be_made_true_equation(value, numbers[1:], acc + num, acc_string+"+"+str(num))  

def can_be_made_true_equation_with_3_op(value, numbers, acc=0,acc_string=""):
    if acc == value and len(numbers) == 0:
        print(f"Equation: {value} == {acc_string}")
        return True
    if acc > value:
        return False
    if len(numbers) == 0:
        return False
    # Explore combinations
    num = numbers[0]
    return can_be_made_true_equation_with_3_op(value, numbers[1:], acc*num, acc_string+"*"+str(num)) or can_be_made_true_equation_with_3_op(value, numbers[1:], acc + num, acc_string+"+"+str(num)) or can_be_made_true_equation_with_3_op(value, numbers[1:], int(str(acc) + str(num)), acc_string+"||"+str(num))


def get_pbm_1(problem):
    sum_true_equations = 0
    for key, number_list in problem.items():
        if can_be_made_true_equation(key, number_list[1:], number_list[0], str(number_list[0])):
            print(f"Key: {key}, Value: {number_list}")
            sum_true_equations += int(key)

    return sum_true_equations

def get_pbm_2(problem):
    sum_true_equations = 0
    for key, number_list in problem.items():
        if can_be_made_true_equation_with_3_op(key, number_list[1:], number_list[0], str(number_list[0])):
            print(f"Key: {key}, Value: {number_list}")
            sum_true_equations += int(key)

    return sum_true_equations


def main():
    problem = read_input("2024/day_7/input.txt")

    print(f"Problem: {problem}")
    sum_true_equations = get_pbm_1(problem)

    print(f"Number of true equations: {sum_true_equations}")

    sum_true_with_3_op = get_pbm_2(problem)
    print(f"Number of true equations with 3 ops: {sum_true_with_3_op}")

main()