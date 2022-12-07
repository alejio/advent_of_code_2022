import os.path
import re


def load_data() -> str:
    with open("data/input") as f:
        list_of_lines = [line.strip() for line in f]
    return list_of_lines


def find_indices(list_to_check: list, pattern: str):
    indices = []
    directories = []
    for idx, value in enumerate(list_to_check):
        match = re.search(pattern, value)
        if match:
            indices.append(idx)
            directories.append(match.groups()[0])
    return indices, directories


def directory_block_paths(data: list) -> list:
    cd_indices, directories = find_indices(data, "^\$ cd (.*)")
    path = []
    for i in range(1, len(directories)+1):
        proc_dir = "/".join(directories[:i])
        path.append(os.path.normpath(proc_dir))
    paths = [i.replace("//", "/") for i in path]
    groups = []
    for idx in range(len(cd_indices)):
        try:
            group = data[cd_indices[idx]:cd_indices[idx+1]]
        except IndexError:
            group = data[cd_indices[idx]:]
        groups.append(group)
    return list(zip(paths, groups))


def directory_size_calculator(block: list) -> int:
    total_size = 0
    for line in block:
        digits_list = ([int(i) for i in line.strip().split() if i.isdigit()])
        if len(digits_list) == 1:
            total_size += digits_list[0]
    return total_size


def dir_filter(name_sizes: list) -> list:
    result = []
    for i in name_sizes:
        if i[1] <= 100000:
            result.append(i)
    return result



def calculate_full_dir_size(names_sizes: list) -> int:
    # Calculate all directories
    dirs = [i[0] for i in names_sizes]
    result = []
    for directory in dirs:
        new_size = 0
        for elem in names_sizes:
            if elem[0].startswith(directory):
                new_size += elem[1]
        result.append([directory, new_size])
    result = list(set([(i[0], i[1]) for i in result]))
    return result



if __name__ == "__main__":
    data = load_data()
    directory_blocks = directory_block_paths(data)
    result = []
    for block in directory_blocks:
        directory_name = block[0]
        directory_contents = block[1]
        size = directory_size_calculator(directory_contents)
        result.append([directory_name, size])
    out = calculate_full_dir_size(result)
    filtered_directories = dir_filter(out)
    print(filtered_directories)
    print(sum([i[1] for i in filtered_directories]))