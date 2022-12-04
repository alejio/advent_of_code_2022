def load_data() -> list:
    with open("data/input") as f:
        list_of_lines = [line.strip().split(",") for line in f]
    return list_of_lines


def full_overlap_checker(range_1: str, range_2: str) -> bool:
    range_1 = range_1.split("-")
    range_1_proc = range(int(range_1[0]), int(range_1[1])+1)
    range_2 = range_2.split("-")
    range_2_proc = range(int(range_2[0]), int(range_2[1])+1)
    check_subset_1 = set(range_1_proc).issubset(range_2_proc)
    check_subset_2 = set(range_2_proc).issubset(range_1_proc)
    return check_subset_1 or check_subset_2


if __name__ == "__main__":
    data = load_data()
    overlap_counter = 0
    for chores in data:
        if full_overlap_checker(*chores) is True:
            overlap_counter += 1
    print(overlap_counter)