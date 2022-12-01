
def load_data():
    with open("data/input") as f:
        lines = [line for line in f]
    return lines


def parse_to_list_of_lists(lines):
    lists = [[]]
    for line in lines:
        if line == "\n":
            lists.append([])
        else:
            lists[-1].append(int(line))
    return lists


def get_max(list_of_lists):
    return max([sum(l) for l in list_of_lists])


def get_total_for_three_elves(list_of_lists):
    calories_per_elf = [sum(l) for l in list_of_lists]
    calories_per_elf.sort(reverse=True)
    return sum(calories_per_elf[0:3])

def main():
    data = load_data()
    list_of_lists = parse_to_list_of_lists(data)
    max_calories = get_max(list_of_lists)
    print(max_calories)
    print(get_total_for_three_elves(list_of_lists))


if __name__ == "__main__":
    main()