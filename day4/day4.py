def load_data() -> list:
    with open("data/input") as f:
        list_of_lines = [line.strip().split(",") for line in f]
    return list_of_lines


def overlap_checker(range_1: str, range_2: str, full: bool) -> bool:
    range_1 = range_1.split("-")
    range_1_proc = range(int(range_1[0]), int(range_1[1])+1)
    range_2 = range_2.split("-")
    range_2_proc = range(int(range_2[0]), int(range_2[1])+1)
    if full is True:
        check_subset_1 = set(range_1_proc).issubset(range_2_proc)
        check_subset_2 = set(range_2_proc).issubset(range_1_proc)
        overlap = check_subset_1 or check_subset_2
    else:
        intersection = set(range_1_proc).intersection(set(range_2_proc))
        if len(intersection) == 0:
            overlap = False
        else:
            overlap = True
    return overlap


if __name__ == "__main__":
    data = load_data()
    full_overlap_counter = 0
    partial_overlap_counter = 0
    for chores in data:
        if overlap_checker(*chores, True) is True:
            full_overlap_counter += 1
        if overlap_checker(*chores, False) is True:
            partial_overlap_counter += 1
    print(full_overlap_counter)
    print(partial_overlap_counter)