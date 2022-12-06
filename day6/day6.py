def load_data() -> str:
    with open("data/input") as f:
        list_of_lines = [line.strip().split(",") for line in f]
    return list_of_lines[0][0]


def identify_start_of_packet_sequence(sequence: str) -> int:
    groups_of_4 = [(sequence[i:i + 4]) for i in range(0, len(sequence)-3)]
    sets = [len(set(group)) for group in groups_of_4]
    first_occurence_idx = sets.index(4)
    return first_occurence_idx + 4


if __name__ == "__main__":
    signal = load_data()
    print(identify_start_of_packet_sequence(signal))