import re

def read_input(file_path: str) -> list:
    """
    Read a file line by line and return each line in a list of string
    """
    with open(file_path, "r") as file:
        return file.readlines()
    
def get_line_mul_score(line: str) -> int:
    """
        Read a line and return the multiplication of the number for each mul instruction 
    """
    score = 0
    # Capture all iteration matching the regex pattern: mul
    # matchs = re.match(r"mul\(([1-9]{1,3}), ([1-9]{1,3})\)", line) 
    # print(f'matchs: {matchs}')

    for i in range(len(line)):
        if line[i:i+4] == 'mul(':
            a, b = 0, 0
            print(f'match mul at index {i} {line[i:i+12]} {score}')
            for j in range(4):
                if line[i+4+j] == ',':
                    a = int(line[i+4:i+4+j])
                    print(f'match a {j} {line[i+4:i+4+j]} {a}')
                    for k in range(4):
                        if line[i+4+j+k+1] == ')':
                            b = int(line[i+4+j+1:i+4+j+k+1])
                            print(f'match b {k} {line[i+4+j+1:i+4+j+k+1]} {b}')
                            score += a*b
                            print(f'score update {a*b} {score}')
                            break
    return score   

def get_line_mul_score_modified(line: str) -> int:
    """
        Read a line and return the multiplication of the number for each mul instruction 
    """
    score = 0
    is_activated = True

    for i in range(len(line)):
        if line[i:i+4] == 'do()':
            is_activated = True
            print(f"{line[i:i+4]}  - do() activated {is_activated}")
            continue
        if line[i:i+7] == "don't()":
            is_activated = False
            print(f"{line[i:i+7]} - don't() activated {is_activated}")
            continue
        if line[i:i+4] == 'mul(':
            a, b = 0, 0
            print(f'match mul at index {i} {line[i:i+12]} {score}')
            for j in range(4):
                if line[i+4+j] == ',':
                    a = int(line[i+4:i+4+j])
                    print(f'match a {j} {line[i+4:i+4+j]} {a}')
                    for k in range(4):
                        if line[i+4+j+k+1] == ')':
                            b = int(line[i+4+j+1:i+4+j+k+1])
                            print(f'match b {k} {line[i+4+j+1:i+4+j+k+1]} {b}')
                            if is_activated:
                                score += a*b
                                print(f'score update {a*b} {score}')
                            else:
                                print(f'score not update because not activated {a*b} {score}')
                            break
    return score   

def main():
    lines = read_input("2024/day_3/input.txt")
    total_score = sum([get_line_mul_score(line) for line in lines])
    print(f"Total score: {total_score}")

    all_instructions = ""
    for line in lines:
        all_instructions += line
    total_score = get_line_mul_score_modified(all_instructions)
    print(f"Total score modified: {total_score}")
main()