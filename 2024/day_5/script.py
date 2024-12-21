

def read_input(file_path: str):
    """
    Read input of the form and give the result in two list pne for each part of the input.
    Form:
    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        ordering, sequences = [], []
        for line in lines:
            if "|" in line:
                ordering.append(list(map(int, line.strip().split("|"))))
            elif "," in line:
                sequences.append(list(map(int, line.strip().split(",")))) 
        return ordering, sequences
    

def is_valid_sequence(ordering: list, sequence: list) -> bool:
    """
    Check if a sequence is valid according to the ordering
    """
    for i in range(len(ordering)):
        if ordering[i][0] in sequence and ordering[i][1] in sequence:
            if sequence.index(ordering[i][0]) > sequence.index(ordering[i][1]):
                return False
    return True

def get_middle_element(sequence: list) -> int:
    """
    Get the middle element of a sequence
    """
    return sequence[len(sequence)//2]

def update_sequence(ordering: list, sequence: list) -> list:
    """
        Return a new sequence with the ordering applied
    """
    if len(sequence) == 1 or len(sequence) == 0:
        return sequence

    elem = sequence[0]
    above, under, not_related = get_above_and_under(ordering, sequence[1:], elem)
    # print(f'not related {elem} {not_related} {above} {under}')
    if len(not_related) > 0:
        print('not related {elem} {not_related}')
    
    return update_sequence(ordering, under) + [elem] + update_sequence(ordering, above)


def get_above_and_under(ordering: list, sequence: list, elem: int):
    """
    Get the elements above and under and not related a given element in the sequence
    """
    above, under, not_related = [], [], []
    for i in range(len(sequence)):
        for j in range(len(ordering)):
            compared = False
            if elem in ordering[j] and sequence[i] in ordering[j]:
                # no duplicate assumption
                if sequence[i] == ordering[j][0]:
                    under.append(sequence[i])
                    compared = True
                    break
                else:
                    above.append(sequence[i])
                    compared = True
                    break
        if not compared:
            not_related.append(sequence[i])
    return above, under, not_related    

def main():
    ordering, sequences = read_input("2024/day_5/input.txt")
    print(f"ordering: {ordering}")
    print(f"sequences: {sequences}")

    valid_sequences = [sequence for sequence in sequences if is_valid_sequence(ordering, sequence)]
    print(f"Number of valid sequences: {len(valid_sequences)}")

    middle_elements = [get_middle_element(sequence) for sequence in valid_sequences]
    print(f"Middle elements: {middle_elements}")

    print(f"Sum of middle elements: {sum(middle_elements)}")

    invalid_sequences = [sequence for sequence in sequences if not is_valid_sequence(ordering, sequence)]
    print(f"Number of invalid sequences: {len(invalid_sequences)}")

    updated_sequences = [update_sequence(ordering, sequence) for sequence in invalid_sequences]
    print(f"Updated sequences: {updated_sequences} - modified from {invalid_sequences}")

    middle_elements_updated = [get_middle_element(sequence) for sequence in updated_sequences]
    print(f"Middle elements updated: {middle_elements_updated}")
    print(f"Sum of middle elements updated: {sum(middle_elements_updated)}")


main()