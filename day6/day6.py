def load_data() -> str:
    with open("data/input") as f:
        list_of_lines = [line.strip().split(",") for line in f]
    return list_of_lines[0][0]


def identify_start_of_sequence(sequence: str, n_distinct_chars: int) -> int:
    groups_of_n = [(sequence[i:i + n_distinct_chars]) for i in range(0, len(sequence)-(n_distinct_chars - 1))]
    sets = [len(set(group)) for group in groups_of_n]
    first_occurence_idx = sets.index(n_distinct_chars)
    return first_occurence_idx + n_distinct_chars


if __name__ == "__main__":
    signal = load_data()
    print(identify_start_of_sequence(signal, 4))
    print(identify_start_of_sequence(signal, 14))