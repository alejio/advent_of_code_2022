import string


def load_data() -> list:
    with open("data/input") as f:
        list_of_lines = [line.strip() for line in f]
    return list_of_lines


def split_rucksack_contents_to_compartments(rucksack_contents: str) -> tuple:
    n_items = len(rucksack_contents)
    compartment_size = int(n_items/2)
    first_compartment = rucksack_contents[0:compartment_size]
    second_compartment = rucksack_contents[compartment_size:]
    return first_compartment, second_compartment


def common_item_type(first_compartment: str,
                     second_compartment: str) -> str:
    return list(set(first_compartment).intersection(set(second_compartment)))[0]


def priority_calculator(item: str) -> int:
    alphabet = string.ascii_letters
    position = alphabet.rfind(item)
    return position + 1


def split_rucksacks_into_groups(rucksacks: list) -> list:
    return [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]


def common_item_type_in_groups(rucksack_group: list) -> str:
    return list(set(rucksack_group[0]).intersection((set(rucksack_group[1]))).intersection(set(rucksack_group[2])))[0]


if __name__ == "__main__":
    rucksacks = load_data()
    sum_common_item_priorities = 0
    for rucksack_contents in rucksacks:
        first_compartment, second_compartment = split_rucksack_contents_to_compartments(rucksack_contents)
        common_item = common_item_type(first_compartment, second_compartment)
        priority = priority_calculator(common_item)
        sum_common_item_priorities += priority
    print(sum_common_item_priorities)
    elf_rucksack_groups = split_rucksacks_into_groups(rucksacks)
    sum_common_item_priorities_v2 = 0
    for group in elf_rucksack_groups:
        common_item_in_group = common_item_type_in_groups(group)
        priority_v2 = priority_calculator(common_item_in_group)
        sum_common_item_priorities_v2 += priority_v2
    print(sum_common_item_priorities_v2)

