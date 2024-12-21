
def read_input(file_path: str) -> (list, list):
    """
        Read a file of the format:
        18102   93258
        34171   50404
        48236   60718
        and return 2 lists of integers, one for each column
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        col1, col2 = [], []
        for line in lines:
            a, b = line.strip().split()
            col1.append(int(a))
            col2.append(int(b))
        return col1, col2

def get_similarity_score(sorted_col1: list, sorted_col2: list) -> int:
    """
        Get the similarity score between 2 sorted columns
    """
    score = 0

    nb_appearances = {}
    for i in range(len(sorted_col2)):
        if sorted_col2[i] in nb_appearances:
            nb_appearances[sorted_col2[i]] += 1
        else:
            nb_appearances[sorted_col2[i]] = 1
    
    for i in range(len(sorted_col1)):
        if sorted_col1[i] in nb_appearances and nb_appearances[sorted_col1[i]] > 0:
            score += sorted_col1[i]*nb_appearances[sorted_col1[i]]
        else:
            score += 0
    return score

def main():
    col1, col2 = read_input("2024/day_1/input.txt")

    col1_sorted = sorted(col1)
    col2_sorted = sorted(col2)

    diff = 0
    for i in range(len(col1)):
        diff += abs(col1_sorted[i] - col2_sorted[i])

    print(f"Sum of differences: {diff}")

    score = get_similarity_score(col1_sorted, col2_sorted)

    print(f"Similarity score: {score}")
    
main()