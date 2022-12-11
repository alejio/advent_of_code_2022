import math


def load_data(dataset: str="input") -> str:
    if dataset == "input":
        filename = "data/input"
    elif dataset == "test_part_1":
        filename = "data/test_input_part_1"
    elif dataset == "test_part_2":
        filename = "data/test_input_part_2"
    with open(filename) as f:
        list_of_lines = [line.strip() for line in f]
    return list_of_lines


def update_head_position(starting_position: tuple, direction: str, distance: int) -> tuple:
    if direction == "L":
        return starting_position[0], starting_position[1] - distance
    elif direction == "R":
        return starting_position[0], starting_position[1] + distance
    elif direction == "U":
        return starting_position[0] - distance, starting_position[1]
    elif direction == "D":
        return starting_position[0] + distance, starting_position[1]
    else:
        raise Exception


def update_tail_position(starting_tail_position: tuple, head_position: tuple) -> tuple:
    square_root_distance = math.sqrt((head_position[1] - starting_tail_position[1]) ** 2 +
                                     (head_position[0] - starting_tail_position[0]) ** 2)

    if square_root_distance <= math.sqrt(2.0):
        return starting_tail_position
    else:
        if head_position[0] == starting_tail_position[0]:
            i = starting_tail_position[0]
            if head_position[1] > starting_tail_position[1]:
                return i, starting_tail_position[1] + 1
            elif head_position[1] < starting_tail_position[1]:
                return i, starting_tail_position[1] - 1
            else:
                raise Exception
        elif head_position[0] > starting_tail_position[0]:
            i = starting_tail_position[0] + 1
            if head_position[1] == starting_tail_position[1]:
                return i, starting_tail_position[1]
            elif head_position[1] > starting_tail_position[1]:
                return i, starting_tail_position[1] + 1
            else:
                return i, starting_tail_position[1] - 1
        else:
            i = starting_tail_position[0] - 1
            if head_position[1] == starting_tail_position[1]:
                return i, starting_tail_position[1]
            elif head_position[1] > starting_tail_position[1]:
                return i, starting_tail_position[1] + 1
            else:
                return i, starting_tail_position[1] - 1


def calculate_distinct_position_visits(tail_trace: list) -> int:
    return len(set(tail_trace))


def main_part_1(movements: list) -> int:
    head_position = (0, 0)
    tail_position = (0, 0)
    head_trace = []
    tail_trace = []
    for movement in movements:
        direction, distance = movement.split(" ")
        distance = int(distance)
        for _ in range(distance):
            head_trace.append(head_position)
            tail_trace.append(tail_position)
            head_position = update_head_position(head_position, direction, 1)
            tail_position = update_tail_position(tail_position, head_position)
    distinct_positions_visited = calculate_distinct_position_visits(tail_trace)
    return distinct_positions_visited


def main_part_2(movements: list) -> int:
    head_position = (0, 0)
    tail_positions = (((0,0), ) * 9)
    head_trace = []
    tail_trace = []
    for movement in movements:
        direction, distance = movement.split(" ")
        distance = int(distance)
        for _ in range(distance):
            head_trace.append(head_position)
            tail_trace.append(tail_positions)
            head_position = update_head_position(head_position, direction, 1)
            new_tail_positions = []
            temp_head_position = head_position
            for tail_position in tail_positions:
                tail_position = update_tail_position(tail_position, temp_head_position)
                temp_head_position = tail_position
                new_tail_positions.append(tail_position)
            tail_positions = tuple(new_tail_positions)
    tail_trace = [t[-1] for t in tail_trace]
    distinct_positions_visited = calculate_distinct_position_visits(tail_trace)
    return distinct_positions_visited


if __name__ == "__main__":
    movements = load_data("input")
    output_part_1 = main_part_1(movements)
    output_part_2 = main_part_2(movements)
    print(output_part_1)
    print(output_part_2)



